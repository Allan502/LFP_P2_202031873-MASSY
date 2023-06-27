import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from PIL import ImageTk, Image
import os
import graphviz
from vistas.arbol import DerivationTreeGraph

class PantallaArbol(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.pantallaParent.automatasCargadosAFN
        self.gramatica=[]
        self.geometry("640x480")
        self.title("Pantalla Arbol")

        tk.Label(self, text="Seleccione una Gramatica").pack(expand=True)
        print(self.automataAFN)
        automatas = [automata[0] for automata in self.automataAFN]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()

        tk.Button(self, text="Aceptar", width=100, height=5, command=self.mostrarArbol).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)
    
    def cerrar_ventana(self):
        self.destroy()
        
    def abrir_ventanaGraficarArbol(self,gramatica):
        print(gramatica)
        ventanaA = DerivationTreeGraph(gramatica)
        ventanaA.grab_set()
        
    def mostrarArbol(self):
        
        automataSeleccionado=self.combobox.get()
        for automataAFN in self.pantallaParent.pantallaParent.automatasCargadosAFN:
            if automataAFN[0] == automataSeleccionado:
                automataSeleccionado=automataAFN
                self.gramatica=automataAFN
                graficoArbol=DerivationTreeGraph(self.gramatica)
                graficoArbol.generate_tree([])
                break




        