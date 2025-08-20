# Comparación de Algoritmos de Búsqueda

Una aplicación gráfica que compara el rendimiento de los algoritmos de búsqueda lineal y binaria mediante una interfaz visual construida con Tkinter y Matplotlib.

## 🚀 Características

- Generación de listas de números aleatorios de diferentes tamaños
- Implementación de búsqueda lineal y binaria
- Medición de tiempos de ejecución en milisegundos
- Visualización gráfica comparativa del rendimiento
- Interfaz gráfica intuitiva y fácil de usar

## 📋 Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

Instalar dependencias:
bash
pip install -r requirements.txt
Nota para usuarios de Ubuntu/Debian: Si tienes problemas con tkinter, instálalo con:
bash
sudo apt-get install python3-tk

🎮 Uso

Ejecución del programa

bash
python main.py
Instrucciones de uso:

Seleccionar tamaño de lista: Elige entre 100, 1000, 5000 o 10000 elementos
Generar datos: Haz clic en "Generar datos" para crear la lista aleatoria
Ingresar valor: Escribe el número que deseas buscar
Ejecutar búsquedas:
Usa "Búsqueda Lineal" para probar el algoritmo lineal
Usa "Búsqueda Binaria" para probar el algoritmo binario
Ver resultados: Los resultados se mostrarán en la parte inferior
Generar gráfica comparativa: Haz clic en el botón para ver la comparación visual
📊 Funcionalidades

Generación de datos: Crea listas ordenadas de números aleatorios
Búsqueda en tiempo real: Ejecuta búsquedas y mide el tiempo de ejecución
Resultados detallados: Muestra el índice encontrado y tiempo promedio
Gráfica comparativa: Visualiza el rendimiento de ambos algoritmos en diferentes tamaños de lista
🏗️ Estructura del Proyecto

text
├── main.py              # Archivo principal de la aplicación
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
└── .gitignore          # Archivos a ignorar en Git
📈 Algoritmos Implementados

🔍 Búsqueda Lineal

Complejidad temporal: O(n)
Recorre cada elemento de la lista secuencialmente
Funciona con listas no ordenadas
🔍 Búsqueda Binaria

Complejidad temporal: O(log n)
Requiere lista ordenada
Divide repetidamente el espacio de búsqueda a la mitad
🐛 Solución de Problemas

Error: "No module named 'tkinter'"

Solución: Instalar tkinter según tu sistema operativo:

Ubuntu/Debian: sudo apt-get install python3-tk
Windows: Reinstalar Python marcando la opción "tcl/tk and IDLE"
macOS: Usar Homebrew: brew install python-tk
Error: "Matplotlib backend issues"

Solución: El código ya fuerza el backend TkAgg, pero si persisten problemas:

bash
pip install --upgrade matplotlib
📝 Personalización

Puedes modificar los tamaños de lista disponibles editando la línea:

python
combo_tamano = ttk.Combobox(frame_inputs, values=[100, 1000, 5000, 10000], width=12)





