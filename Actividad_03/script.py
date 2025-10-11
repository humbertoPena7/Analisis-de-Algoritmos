"""
TMAP visualization and subcluster analysis on Fashion MNIST
"""

import base64
from io import BytesIO
from timeit import default_timer as timer

import numpy as np
import umap

CFG = {"n_neighbors": 15, "min_dist": 0.1, "metric": "euclidean"}

from faerun import Faerun
from PIL import Image
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import fashion_mnist

(IMAGES_TRAIN, LABELS_TRAIN), (IMAGES_TEST, LABELS_TEST) = fashion_mnist.load_data()

# Flatten images (28x28 to 784) for TMAP
IMAGES_TRAIN = IMAGES_TRAIN.reshape(len(IMAGES_TRAIN), -1)
IMAGES_TEST = IMAGES_TEST.reshape(len(IMAGES_TEST), -1)

IMAGES = np.concatenate((IMAGES_TRAIN, IMAGES_TEST))
LABELS = np.concatenate((LABELS_TRAIN, LABELS_TEST))
IMAGE_LABELS = []

LABEL_NAMES = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]


def main():
    print("Convirtiendo imágenes ...")
    for image in IMAGES:
        img = Image.fromarray(image.reshape(28, 28).astype(np.uint8))
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        IMAGE_LABELS.append(
            "data:image/bmp;base64," + str(img_str).replace("b'", "").replace("'", "")
        )

    tmp = (IMAGES / 255).astype(np.float32)

    print("Ejecutando UMAP global ...")
    start = timer()
    reducer = umap.UMAP(n_neighbors=CFG["n_neighbors"], min_dist=CFG["min_dist"], metric=CFG["metric"])
    embedding = reducer.fit_transform(tmp)
    x, y = embedding[:, 0], embedding[:, 1]
    s, t = None, None  # UMAP does not produce a tree; tree edges ignored
    print("umap global:", str(timer() - start))

    # Visualización Global
    faerun = Faerun(clear_color="#111111", view="front", coords=False)
    faerun.add_scatter(
        "FMNIST_Global",
        {"x": x, "y": y, "c": LABELS, "labels": IMAGE_LABELS},
        colormap="tab10",
        shader="smoothCircle",
        point_scale=2.5,
        max_point_size=10,
        has_legend=True,
        categorical=True,
        legend_labels=list(enumerate(LABEL_NAMES)),
    )
    faerun.add_tree("FMNIST_tree", {"from": [], "to": []}, point_helper="FMNIST_Global", color="#666666")
    faerun.plot("fmnist_global", template="url_image")

    # ========================================
    # Seleccion del cluster (Sandal)
    # ========================================

    cluster_label = 5  # Cambiar para otro cluster (0–9)
    cluster_name = LABEL_NAMES[cluster_label]
    print(f"\nAnalizando subclusters del cluster '{cluster_name}' ...")

    mask = LABELS == cluster_label
    images_cluster = IMAGES[mask]
    labels_cluster = LABELS[mask]

    # Convertir imagenes del cluster a base64 para usarlas como labels
    IMAGE_LABELS_CLUSTER = []
    for image in images_cluster:
        img = Image.fromarray(image.reshape(28, 28).astype(np.uint8))
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        IMAGE_LABELS_CLUSTER.append(
            "data:image/bmp;base64," + str(img_str).replace("b'", "").replace("'", "")
        )

    # ========================================
    # Reaplicar UMAP
    # ========================================

    tmp_sub = (images_cluster / 255).astype(np.float32)
    reducer_sub = umap.UMAP(n_neighbors=CFG["n_neighbors"], min_dist=CFG["min_dist"], metric=CFG["metric"])
    embedding_sub = reducer_sub.fit_transform(tmp_sub)
    x_sub, y_sub = embedding_sub[:, 0], embedding_sub[:, 1]
    s_sub, t_sub = None, None  # UMAP does not produce a tree; tree edges ignored

    # ========================================
    # Visualizar subclusters (KMeans)
    # ========================================
    from sklearn.cluster import KMeans
    # Choose number of subclusters (e.g., 5)
    n_subclusters = 5
    kmeans = KMeans(n_clusters=n_subclusters, random_state=42)
    subcluster_labels = kmeans.fit_predict(embedding_sub)

    faerun = Faerun(clear_color="#111111", view="front", coords=False)
    faerun.add_scatter(
        f"FMNIST_{cluster_name}",
        {"x": x_sub, "y": y_sub, "c": subcluster_labels, "labels": IMAGE_LABELS_CLUSTER},
        colormap="plasma",
        shader="smoothCircle",
        point_scale=3.0,
        max_point_size=12,
        has_legend=False,
        categorical=True,
    )
    # UMAP does not produce a tree; skip or simulate empty tree
    faerun.add_tree(
        f"FMNIST_{cluster_name}_tree",
        {"from": [], "to": []},
        point_helper=f"FMNIST_{cluster_name}",
        color="#777777"
    )
    faerun.plot(f"fmnist_{cluster_name.lower()}", template="url_image")

    print("Mostrando imágenes representativas del cluster...")
    indices = np.random.choice(len(images_cluster), size=25, replace=False)
    sample_images = images_cluster[indices]

    plt.figure(figsize=(8, 8))
    for i, img in enumerate(sample_images):
        plt.subplot(5, 5, i + 1)
        plt.imshow(img.reshape(28, 28), cmap="gray")
        plt.axis("off")
    plt.suptitle(f"Muestras representativas del cluster '{cluster_name}'", fontsize=14)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
