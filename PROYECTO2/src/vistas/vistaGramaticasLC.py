import tkinter as tk
from vistas.vistaCargaGramatica import PantallaCargaGramatica
from vistas.vistaMostrarGramatica import PantallaMostrarGramatica
from vistas.vistaArbol import PantallaArbol

class PantallaGramaticasLC(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.automatasCargadosAFN
        self.geometry("6400x4800")
        self.title("Gramaticas Libres de Contexto")

        tk.Button(self, text="Cargar Archivo", width=100, height=5, command=self.abrir_ventanaCargaGramatica).pack(
            expand=True
        )
        tk.Button(self, text="Mostrar Informacion General", width=100, height=5, command=self.abrir_ventanaMostrarGramatica).pack(
            expand=True
        )
        tk.Button(self, text="Arbol de Derivacion", width=100, height=5, command=self.abrir_ventanaAbrirArbol).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaGramaticasLC.destroy(self)
        
    def abrir_ventanaCargaGramatica(self):
        ventanaCG = PantallaCargaGramatica(self)
        ventanaCG.grab_set()
        
    def abrir_ventanaMostrarGramatica(self):
        ventanaMG = PantallaMostrarGramatica(self)
        ventanaMG.grab_set()
        
    def abrir_ventanaAbrirArbol(self):
        ventanaAA = PantallaArbol(self)
        ventanaAA.grab_set()