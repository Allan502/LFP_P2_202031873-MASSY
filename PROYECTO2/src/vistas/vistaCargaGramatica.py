import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Gramatica.DataGramatica import DataGramatica, ProduccionesGramatica
import graphviz
from PIL import ImageTk, Image
import os


class PantallaCargaGramatica(tk.Toplevel):
    pantallaParent=None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent

        self.geometry("640x480")
        self.title("Carga de Gramatica")

        tk.Button(self, text="Cargar Gramatica", width=100, height=5, command = self.cargarGramatica).pack(
            expand=True
        )
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaCargaGramatica.destroy(self)

    def cargarGramatica(self):
        gramaticas = []
        automataActual=None
        dataAutomataActual=None
        estadoAutomata=None
        alfabetoAutomata=None
        estadoInicialAutomata=None
        estadoAceptacionAutomata=None
        produccionesArray=[]
        noTerminalProduccionActual=""
        
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.glc")])
        with open(nombre_archivo, "r") as archivo:
            contador = 0
            for linea in archivo:
                linea = linea.rstrip()
                #print(linea)
                contador += 1
                if contador==1:
                    automataActual=linea
                    dataAutomataActual=DataGramatica()
                elif contador==2:
                    estados=linea.split(",")
                    for state in estados:
                        dataAutomataActual.noTerminales.append(state)
                elif contador==3:
                    alfabeto=linea.split(",")
                    for alfabet in alfabeto:
                        dataAutomataActual.terminales.append(alfabet)
                elif contador==4:
                    estadoInicialAutomata=linea
                    dataAutomataActual.noTerminalInicial=estadoInicialAutomata
                if("::=" in linea):
                    #encontramos una transicion porque hay un ;
                    if "::=" in linea:
                        produccion=linea.split("::=")
                        nombreProduccion=[produccion[0]]
                        noTerminalProduccionActual=nombreProduccion
                    else:
                        produccion=linea.split("|")
                        nombreProduccion=[noTerminalProduccionActual]
                    partesProduccion=produccion[1].split(" ")
                    produccion=nombreProduccion + partesProduccion
                    dataAutomataActual.producciones.append(produccion)
                    '''estados=linea.split(" ")
                    transicionActual=ProduccionesGramatica(estados[0], estados[1]).transform()
                    dataAutomataActual.producciones.append(transicionActual)'''
                """ elif("," in linea):
                    print("Mostrar separacion")
                    estados=linea.split(",")
                    for estado in estados:
                        print(estado)
                    print("Fin separacion") """
                if("%" in linea):
                    gramaticas.append([automataActual, dataAutomataActual.noTerminales,dataAutomataActual.terminales,dataAutomataActual.noTerminalInicial, dataAutomataActual.producciones])
                    contador=0
                    automataActual=None
                    dataAutomataActual=None
                    estadoAutomata=None
                    alfabetoAutomata=None
                    estadoInicialAutomata=None
                    estadoAceptacionAutomata=None
                    produccionesArray=[]
                    
        messagebox.showinfo("Mensaje Emergente", "cargado con exito")
        self.pantallaParent.pantallaParent.automatasCargadosAFN.extend(gramaticas)
        print(self.pantallaParent.pantallaParent.automatasCargadosAFN)
        print(gramaticas)
        '''arrayGramaticas=gramaticas
        print(arrayGramaticas[0][0])
        print(arrayGramaticas[0][1])
        print(arrayGramaticas[0][2])
        print(arrayGramaticas[0][3])
        print(arrayGramaticas[0][4])'''
        
  