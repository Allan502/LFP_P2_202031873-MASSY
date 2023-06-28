import tkinter as tk
from vistas.vistaCargaAutomataPila import PantallaCargaAutomataPila
from vistas.vistaMostrarAutomataPila import PantallaMostrarAP
from vistas.vistaSeleccionarAP import PantallaSeleccionarAFD
from vistas.vistaSeleccionarAPR import PantallaSeleccionarAFDR
from vistas.vistaSeleccionarAPRecorrido import PantallaSeleccionarAPRecorrido
from vistas.vistaSeleccionarAPPasada import PantallaSeleccionarPasada

class PantallaAutomataPila(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.automatasCargadosAFD
        self.geometry("6400x4800")
        self.title("Automata de Pila")

        tk.Button(self, text="Cargar Archivo", width=100, height=5, command=self.abrir_ventanaCargaAP).pack(
            expand=True
        )
        tk.Button(self, text="Mostrar Informacion de Automata", width=100, height=5, command=self.abrir_ventanaMostrarAP).pack(
            expand=True
        )
        tk.Button(self, text="Validar una Cadena", width=100, height=5, command=self.abrir_ventanaSeleccionarAP).pack(expand=True)
        tk.Button(self, text="Ruta de Validacion", width=100, height=5, command=self.abrir_ventanaSeleccionarAPRuta).pack(expand=True)
        tk.Button(self, text="Recorrido Paso a Paso", width=100, height=5, command=self.abrir_ventanaSeleccionarAPRecorrido).pack(expand=True)
        tk.Button(self, text="Validar Cadena en una Pasada", width=100, height=5, command=self.abrir_ventanaSeleccionarAPPasada).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaAutomataPila.destroy(self)
        
    def abrir_ventanaCargaAP(self):
        ventanaCA = PantallaCargaAutomataPila(self)
        ventanaCA.grab_set()
        
    def abrir_ventanaMostrarAP(self):
        ventanaMAP = PantallaMostrarAP(self)
        ventanaMAP.grab_set()
        
    def abrir_ventanaSeleccionarAP(self):
        ventanaSAP = PantallaSeleccionarAFD(self)
        ventanaSAP.grab_set()
        
    def abrir_ventanaSeleccionarAPRuta(self):
        ventanaSAPR = PantallaSeleccionarAFDR(self)
        ventanaSAPR.grab_set()
        
    def abrir_ventanaSeleccionarAPRecorrido(self):
        ventanaSAPRe = PantallaSeleccionarAPRecorrido(self)
        ventanaSAPRe.grab_set()

    def abrir_ventanaSeleccionarAPPasada(self):
        ventanaPasada = PantallaSeleccionarPasada(self)
        ventanaPasada.grab_set()