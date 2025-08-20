import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import numpy as np
import matplotlib
# Forzar el backend de Matplotlib compatible con tkinter
matplotlib.use("TkAgg")

# ---------------------- Funciones de búsqueda ---------------------- #


def busqueda_lineal(lista, x):
    for i, val in enumerate(lista):
        if val == x:
            return i
    return -1


def busqueda_binaria(lista, x):
    low, high = 0, len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == x:
            return mid
        elif lista[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---------------------- Generación de datos ---------------------- #
datos = []


def generar_datos():
    global datos
    try:
        tamaño = int(combo_tamano.get())
    except ValueError:
        messagebox.showerror("Error", "Seleccione un tamaño válido")
        return

    datos = sorted(np.random.randint(1, tamaño*10, tamaño).tolist())
    texto_datos.delete("1.0", tk.END)
    texto_datos.insert(tk.END, str(datos))
    lbl_resultado.config(text="Datos generados correctamente")

# ---------------------- Medición de tiempo ---------------------- #


def measure_time(func, lista, valor):
    inicio = time.perf_counter()
    func(lista, valor)
    fin = time.perf_counter()
    return (fin - inicio) * 1000  # Convertir a milisegundos

# ---------------------- Ejecución de búsqueda ---------------------- #


def ejecutar_busqueda(tipo):
    if not datos:
        messagebox.showwarning("Atención", "Primero genere los datos")
        return
    try:
        valor = int(entry_valor.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico a buscar")
        return

    repeticiones = 5
    tiempos = []
    resultado = -1

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        if tipo == "lineal":
            resultado = busqueda_lineal(datos, valor)
        else:
            resultado = busqueda_binaria(datos, valor)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)  # ms

    tiempo_promedio = sum(tiempos) / repeticiones
    if resultado == -1:
        texto_res = "No encontrado"
    else:
        texto_res = f"Índice: {resultado}"

    lbl_resultado.config(
        text=f"Tamaño lista: {len(datos)}\n"
        f"{texto_res}\n"
        f"Tiempo promedio: {tiempo_promedio:.5f} ms"
    )

    return tiempo_promedio

# ---------------------- Gráfica comparativa ---------------------- #


def generar_grafica():
    try:
        # INCLUIR EL 5000 en la lista de tamaños para la gráfica
        tamaños_grafica = [100, 1000, 5000, 10000]
        tiempos_lineal = []
        tiempos_binaria = []

        for n in tamaños_grafica:
            lista_temp = sorted(np.random.randint(1, n*10, n).tolist())
            valor_a_buscar = random.choice(lista_temp)

            # Medir tiempos
            tiempo_lineal = np.mean(
                [measure_time(busqueda_lineal, lista_temp, valor_a_buscar) for _ in range(5)])
            tiempo_binaria = np.mean(
                [measure_time(busqueda_binaria, lista_temp, valor_a_buscar) for _ in range(5)])

            tiempos_lineal.append(round(tiempo_lineal, 5))
            tiempos_binaria.append(round(tiempo_binaria, 5))

        ax.clear()
        ax.plot(tamaños_grafica, tiempos_lineal, marker='o',
                label="Búsqueda Lineal", linewidth=2)
        ax.plot(tamaños_grafica, tiempos_binaria, marker='s',
                label="Búsqueda Binaria", linewidth=2)
        ax.set_xlabel("Tamaño de lista")
        ax.set_ylabel("Tiempo (ms)")
        ax.set_title("Comparación de tiempos de búsqueda")
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xscale('log')

        # Agregar etiquetas con los valores exactos
        # ANOTACIONES simplificadas
        for tam, tiempo in zip(tamaños_grafica, tiempos_lineal):
            ax.annotate(f'{tiempo:.5f} ms',
                        (tam, tiempo),
                        textcoords="offset points",
                        xytext=(0, 10),
                        ha='center',
                        fontsize=8)

        for tam, tiempo in zip(tamaños_grafica, tiempos_binaria):
            ax.annotate(f'{tiempo:.5f} ms',
                        (tam, tiempo),
                        textcoords="offset points",
                        xytext=(0, 10),
                        ha='center',
                        fontsize=8)

        fig.tight_layout()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error al graficar", str(e))


# ---------------------- Interfaz gráfica ---------------------- #
root = tk.Tk()
root.title("Comparación de Búsqueda")
root.geometry("950x900")

# Inputs
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10, fill="x")

tk.Label(frame_inputs, text="Tamaño de lista:").grid(row=0, column=0, padx=5)
combo_tamano = ttk.Combobox(
    frame_inputs, values=[100, 1000, 5000, 10000], width=12)
combo_tamano.current(0)
combo_tamano.grid(row=0, column=1, padx=5)
btn_generar = tk.Button(
    frame_inputs, text="Generar datos", command=generar_datos)
btn_generar.grid(row=0, column=2, padx=5)

tk.Label(frame_inputs, text="Valor a buscar:").grid(row=1, column=0, padx=5)
entry_valor = tk.Entry(frame_inputs, width=12)
entry_valor.grid(row=1, column=1, padx=5)

btn_lineal = tk.Button(frame_inputs, text="Búsqueda Lineal",
                       command=lambda: ejecutar_busqueda("lineal"))
btn_lineal.grid(row=1, column=2, padx=5)
btn_binaria = tk.Button(frame_inputs, text="Búsqueda Binaria",
                        command=lambda: ejecutar_busqueda("binaria"))
btn_binaria.grid(row=1, column=3, padx=5)

lbl_resultado = tk.Label(root, text="Resultado aparecerá aquí", justify="left")
lbl_resultado.pack(pady=10)

# Caja de texto para mostrar los números generados
texto_datos = tk.Text(root, height=8, width=110)
texto_datos.pack(pady=5)

# Frame para gráfica
frame_grafica = tk.Frame(root)
frame_grafica.pack(pady=10, fill="both", expand=True)

# Configurar la figura de matplotlib
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

# Botón para generar gráfica
btn_grafica = tk.Button(
    root, text="Generar gráfica comparativa", command=generar_grafica,
    bg="lightblue", font=("Arial", 12, "bold"))
btn_grafica.pack(pady=10)

root.mainloop()
