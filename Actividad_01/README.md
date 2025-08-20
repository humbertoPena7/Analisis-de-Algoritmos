# Comparación de Algoritmos de Búsqueda en Python

Este proyecto implementa y compara el rendimiento de **Búsqueda Lineal** y **Búsqueda Binaria** en Python.  
A través de una **interfaz gráfica** desarrollada con **Tkinter** y **Matplotlib**, el usuario puede:

- Generar listas de números aleatorios.
- Realizar búsquedas de un valor dentro de la lista.
- Comparar los tiempos de ejecución promedio de ambos algoritmos.
- Visualizar gráficamente la diferencia de eficiencia según el tamaño de la lista.

---

## 📌 Características

- **Interfaz gráfica amigable** con Tkinter.  
- **Generación dinámica de datos** ordenados aleatoriamente.  
- **Búsqueda Lineal y Binaria** implementadas manualmente.  
- **Medición de tiempos de ejecución** en milisegundos.  
- **Gráfica comparativa** del rendimiento de ambos algoritmos para distintos tamaños de lista (100, 1000, 5000, 10000 elementos).  

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Tkinter** → Para la interfaz gráfica.  
- **Matplotlib** → Para la generación de gráficas.  
- **NumPy** → Para la generación eficiente de datos aleatorios.  

---

## 📂 Estructura del Proyecto

```
📁 Analisis-de-Algoritmos
│── main.py              # Código principal con la interfaz y algoritmos
│── requirements.txt     # Dependencias necesarias
│── README.md            # Documentación del proyecto
```

---

## ▶️ Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/humbertoPena7/Analisis-de-Algoritmos.git
cd Analisis-de-Algoritmos
```

### 2. Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el programa
```bash
python main.py
```

---

## 📊 Ejemplo de Uso

1. Seleccionar el tamaño de la lista.  
2. Generar los datos con el botón **"Generar datos"**.  
3. Ingresar un valor a buscar.  
4. Ejecutar **Búsqueda Lineal** o **Búsqueda Binaria**.  
5. Visualizar el resultado (índice encontrado o "No encontrado") y el **tiempo promedio de búsqueda**.  
6. Generar la **gráfica comparativa** para ver el rendimiento en distintos tamaños de lista.  

---

## 📖 Conclusiones

- La **Búsqueda Binaria** es considerablemente más eficiente que la **Lineal** en listas grandes.  
- Para listas pequeñas, la diferencia en tiempos es mínima.  
- La eficiencia de la Binaria escala mucho mejor conforme aumenta el tamaño de la lista.  

---

## 👨‍💻 Autor

Proyecto desarrollado por **Humberto de Jesús Peña Dueñas**  
📧 Contacto: humbertodejesuspenaduenas@ejemplo.com  
🔗 Repositorio: [Analisis-de-Algoritmos](https://github.com/humbertoPena7/Analisis-de-Algoritmos.git)
