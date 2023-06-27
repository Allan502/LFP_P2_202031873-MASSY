import tkinter as tk
import graphviz
from PIL import ImageTk, Image
import os

class AutomataPila(tk.Toplevel):
    def __init__(self, automata):
        super().__init__()
        self.geometry("640x480")
        self.title("Pantalla de Automata de Pila")
        #PantallaCrearAFN.get()
        f = graphviz.Graph()

        # Configuración de la fuente
        f.node_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        f.edge_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        print(automata[0])
        print(automata[1])
        print(automata[2])
        print(automata[3])
        print(automata[4])
        print(automata[5])
        print(automata[6])

    
        #Definición de los nodos del círculo (todo tipo de estado
        f.attr('node', shape = 'circle')
        for estado in automata[1]:
            if estado not in automata[4]:
                f.node(estado)
            else: #Definición de los nodos dobles circulares (estados de aceptacion)
                f.attr('node', shape ='doublecircle')
                f.node(estado)
                f.attr('node', shape='circle')


        # Definición de las aristas
        #para cada transicion ejecutar: f.edge(estadoInicial, estadoFinal, label = valorTransicion)
        #Lista de transiciones en formato (estado1, valor, estado2), (estado1, valor, estado2) ...
        for transicion in automata[6]:
            automata[6][0][0], automata[6][0][1], automata[6][0][2], automata[6][0][3], automata[6][0][4], automata[6][0][5], automata[6][0][6] = transicion
            f.edge(automata[6][0][0], automata[6][0][3], label=automata[6][0][1]+","+automata[6][0][2]+";"+automata[6][0][4])


        f.render(automata[0], directory="output", format="png", cleanup=True)
        
        frame = tk.Frame(self, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Cargar la imagen
        imagen = Image.open(os.path.join(os.path.dirname(__file__),  "../../../output/"+automata[0]+".png"))

        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((600, 400))

        # Convertir la imagen a un objeto PhotoImage
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Create a Label Widget to display the text or Image
        label = tk.Label(self, image = self.imagen_tk)
        label.pack()
