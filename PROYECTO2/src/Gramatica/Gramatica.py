import tkinter as tk
import graphviz
from PIL import ImageTk, Image
import os

class Gramatica(tk.Toplevel):
    def __init__(self, gramatica):
        super().__init__()
        self.geometry("640x480")
        self.title("Pantalla de Automata de Pila")
        #PantallaCrearAFN.get()
        f = graphviz.Graph()

        # Configuración de la fuente
        f.node_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        f.edge_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        print(gramatica[0])
        print(gramatica[1])
        print(gramatica[2])
        print(gramatica[3])
        print(gramatica[3][0][0])
        print(gramatica[3][0][1])
        print(gramatica[3][1][0])
        print(gramatica[3][1][1])
 
    
        #Definición de los nodos del círculo (todo tipo de estado
        f.attr('node', shape = 'circle')
        for estado in gramatica[1]:
            if estado not in gramatica[4]:
                f.node(estado)
            else: #Definición de los nodos dobles circulares (estados de aceptacion)
                f.attr('node', shape ='doublecircle')
                f.node(estado)
                f.attr('node', shape='circle')


        # Definición de las aristas
        #para cada transicion ejecutar: f.edge(estadoInicial, estadoFinal, label = valorTransicion)
        #Lista de transiciones en formato (estado1, valor, estado2), (estado1, valor, estado2) ...
        for produccion in gramatica[3]:
            gramatica[3][0][0], gramatica[3][0][1]= produccion
            f.edge(gramatica[3][0][0], label=gramatica[3][0][1])


        f.render(gramatica[0], directory="output", format="png", cleanup=True)
        

