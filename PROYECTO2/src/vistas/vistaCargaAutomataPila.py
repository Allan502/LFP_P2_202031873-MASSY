import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from automataPila.DataAutomataPila import DataAutomataPila, TransicionesAutomataPila
import graphviz
from PIL import ImageTk, Image
import os

class PantallaCargaAutomataPila(tk.Toplevel):
    pantallaParent=None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent

        self.geometry("640x480")
        self.title("Carga de Automata de Pila")

        tk.Button(self, text="Cargar Automata de Pila", width=100, height=5, command = self.cargarAP).pack(
            expand=True
        )
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        PantallaCargaAutomataPila.destroy(self)

    def cargarAP(self):
        automatasAFD = []
        automataActual=None
        dataAutomataActual=None
        estadoAutomata=None
        alfabetoAutomata=None
        estadoInicialAutomata=None
        estadoAceptacionAutomata=None
        
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.ap")])
        with open(nombre_archivo, "r") as archivo:
            contador = 0
            for linea in archivo:
                linea = linea.rstrip()
                #print(linea)
                contador += 1
                if contador==1:
                    automataActual=linea
                    dataAutomataActual=DataAutomataPila()
                elif contador==2:
                    alfabeto=linea.split(",")
                    for alfabet in alfabeto:
                        dataAutomataActual.alfabeto.append(alfabet)
                elif contador==3:
                    simbolosPila=linea.split(",")
                    for symbolP in simbolosPila:
                        dataAutomataActual.simbolosPila.append(symbolP)
                elif contador==4:
                    estados=linea.split(",")
                    for state in estados:
                        dataAutomataActual.estados.append(state)
                elif contador==5:
                    estadoInicialAutomata=linea
                    dataAutomataActual.estadoInicial=estadoInicialAutomata
                elif contador==6:
                    estadoAceptacionAutomata=linea
                    dataAutomataActual.estadoAceptacion=estadoAceptacionAutomata
                elif contador>=7 and "%" not in linea:
                    #encontramos una transicion 
                    print("aqui hice el print")
                    print(automatasAFD)
                    linea = linea.replace(";", ",")
                    transicion=linea.split(",")
                    print("quiero ver la transicion")
                    print(transicion)
                    
                    transicionActual=TransicionesAutomataPila(transicion[0], transicion[1], transicion[2], transicion[3], transicion[4]).transform()
                    dataAutomataActual.transiciones.append(transicionActual)
                    print(dataAutomataActual.transiciones)
                    print("quiero ver la actual")
                    print(transicionActual)
                """ elif("," in linea):
                    print("Mostrar separacion")
                    estados=linea.split(",")
                    for estado in estados:
                        print(estado)
                    print("Fin separacion") """
                if("%" in linea):
                    automatasAFD.append([automataActual, dataAutomataActual.alfabeto,dataAutomataActual.simbolosPila,dataAutomataActual.estados,dataAutomataActual.estadoInicial,dataAutomataActual.estadoAceptacion,dataAutomataActual.transiciones])
                    print("print data atual automata")
                    print(automatasAFD)

                    f = graphviz.Graph()

                    # Configuración de la fuente
                    f.node_attr['fontname'] = 'Helvetica, Arial, sans-serif'
                    f.edge_attr['fontname'] = 'Helvetica, Arial, sans-serif'

    
                    #Definición de los nodos del círculo (todo tipo de estado
                    f.attr('node', shape = 'circle')
                    for estado in dataAutomataActual.estados:
                        if estado not in dataAutomataActual.estadoAceptacion:
                            f.node(estado)
                        else: #Definición de los nodos dobles circulares (estados de aceptacion)
                            f.attr('node', shape ='doublecircle')
                            f.node(estado)
                            f.attr('node', shape='circle')
                    print(automatasAFD)

                    # Definición de las aristas
                    #para cada transicion ejecutar: f.edge(estadoInicial, estadoFinal, label = valorTransicion)
                    #Lista de transiciones en formato (estado1, valor, estado2), (estado1, valor, estado2) ...
                    for transicion in dataAutomataActual.transiciones:
                        f.edge(transicion[0], transicion[3], label=transicion[1]+","+transicion[2]+";"+transicion[4])
                    f.render(automataActual, directory="output", format="png", cleanup=True)
                    print(automatasAFD)
                    contador=0
                    automataActual=None
                    dataAutomataActual=None
                    estadoAutomata=None
                    alfabetoAutomata=None
                    estadoInicialAutomata=None
                    estadoAceptacionAutomata=None
                    print(automatasAFD)
        print("se cargo")
        messagebox.showinfo("Mensaje Emergente", "Automata de Pila cargado con exito")
        self.pantallaParent.pantallaParent.automatasCargadosAFD.extend(automatasAFD)
        print(self.pantallaParent.pantallaParent.automatasCargadosAFD)
        print(automatasAFD)