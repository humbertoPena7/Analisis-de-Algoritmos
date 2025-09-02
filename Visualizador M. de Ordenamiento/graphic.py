import tkinter as tk
from tkinter import ttk
import random
import time
import algorithms

class Graphic():

    def __init__(self, belonging):
        self.ANCHO = 800
        self.ALTO = 300
        self.VAL_MIN, self.VAL_MAX = 5, 100
        self.canvas = tk.Canvas(belonging, width=self.ANCHO, height=self.ALTO, bg="white")
        self.data = []


    def dibujar_barras(self, canvas, isHighlight, activos=None):
        if not isHighlight:
            activos=None
        self.canvas.delete("all")
        if not self.data: return
        n = len(self.data)
        margen = 10
        ancho_disp = self.ANCHO - 2 * margen
        alto_disp = self.ALTO - 2 * margen
        w = ancho_disp / n
        esc = alto_disp / max(self.data)
        for i, v in enumerate(self.data):
            x0 = margen + i * w
            x1 = x0 + w * 0.9
            h = v * esc
            y0 = self.ALTO - margen - h
            y1 = self.ALTO - margen
            color = "#4e79a7"
            if activos and i in activos:
                color = "#f28e2b"
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        canvas.create_text(6, 6, anchor="nw", text=f"n={len(self.data)}", fill="#666")


    def generar(self, num, isHighlight):
        if not isinstance(num, int):
            num = 20
        random.seed(time.time())
        self.data = [random.randint(self.VAL_MIN, self.VAL_MAX) for _ in range(num)]
        self.dibujar_barras(self.canvas, isHighlight)

    def ordenar(self, function, delay, belonging, isHighlight):
        if not self.data:
            return
        gen = function(
            self.data,
            lambda activos=None: self.dibujar_barras(self.canvas, isHighlight, activos)
        )
        def paso():
            try:
                next(gen)
                belonging.after(delay, paso)
            except StopIteration:
                pass
        paso()
    
    def shuffle(self, isHighlight):
        random.shuffle(self.data)
        self.dibujar_barras(self.canvas, isHighlight)

