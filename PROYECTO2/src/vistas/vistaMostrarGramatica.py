import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from PIL import ImageTk, Image
import os

class PantallaMostrarGramatica(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.pantallaParent.automatasCargadosAFN
        self.geometry("640x480")
        self.title("Pantalla Mostrar Gramatica")

        tk.Label(self, text="Seleccione una Gramatica").pack(expand=True)
        print(self.automataAFN)
        automatas = [automata[0] for automata in self.automataAFN]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()

        tk.Button(self, text="Aceptar", width=100, height=5, command=self.generarGramatica).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)
    
    def cerrar_ventana(self):
        self.destroy()

    def generarGramatica(self):
        automataSeleccionado=self.combobox.get()
        for automataAFN in self.pantallaParent.pantallaParent.automatasCargadosAFN:
            if automataAFN[0] == automataSeleccionado:
                automataSeleccionado=automataAFN
                break
        nombre = automataSeleccionado[0]
        noTerminales = str(automataSeleccionado[1])
        terminales = str(automataSeleccionado[2])
        noTerminalInicial = str(automataSeleccionado[3])
        producciones = automataSeleccionado[4]
        
        tk.Label(self, text="Nombre: "+nombre).pack(expand=True)
        tk.Label(self, text="No Terminales: "+noTerminales).pack(expand=True)
        tk.Label(self, text="Terminales: "+terminales).pack(expand=True)
        tk.Label(self, text="No Terminal Inicial: "+noTerminalInicial).pack(expand=True)
        tk.Label(self, text="Producciones: ").pack(expand=True)
        
        for produccion in producciones:
            print(produccion)
            tk.Label(self, text=produccion[0]+"::="+" ".join(produccion[1:])).pack(expand=True)
