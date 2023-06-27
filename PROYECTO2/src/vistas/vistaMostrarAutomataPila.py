import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from PIL import ImageTk, Image
import os

class PantallaMostrarAP(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.pantallaParent.automatasCargadosAFD
        self.geometry("640x480")
        self.title("Pantalla Generar Reporte Automata Pila")

        tk.Label(self, text="Seleccione un Automata de Pila").pack(expand=True)
        automatas = [automata[0] for automata in self.automataAFN]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()

        tk.Button(self, text="Aceptar", width=100, height=5, command=self.generarPDF).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()

    def generarPDF(self):
        automataSeleccionado=self.combobox.get()
        for automataAFN in self.pantallaParent.pantallaParent.automatasCargadosAFD:
            if automataAFN[0] == automataSeleccionado:
                automataSeleccionado=automataAFN
                break
        w, h = A4
        pdf = canvas.Canvas("ReporteAP.pdf", pagesize=A4)
        pdf.setTitle("Reporte de Automata de Pila")
        text = pdf.beginText(50, h-50)
        text.setFont("Times-Roman", 12)
        text.textLine("Nombre:"+automataSeleccionado[0])
        text.textLine("Alfabeto: "+str(automataSeleccionado[1]))
        text.textLine("Alfabeto de Pila: "+str(automataSeleccionado[2]))
        text.textLine("Estados: "+str(automataSeleccionado[3]))
        text.textLine("Estado Inicial: "+str(automataSeleccionado[4]))
        text.textLine("Estado de Aceptacion: "+str(automataSeleccionado[5]))
        text.textLine()
        text.textLine("Automata de Pila generado con Graphviz")
        pdf.drawText(text)
        pdf.drawInlineImage("output/"+automataSeleccionado[0]+".png", 0,h-400, width=200, height=200, preserveAspectRatio=True)
        pdf.save()
        webbrowser.open_new_tab('ReporteAP.pdf')
        





