import tkinter as tk
from tkinter import messagebox
from datos import Datos
from vistas.vistaGramaticasLC import PantallaGramaticasLC
from vistas.vistaAutomataPila import PantallaAutomataPila
import time


class App:
    automatasCargadosAFD=[]
    automatasCargadosAFN=[]
    automatasCargadosAFD_optimizados=[]
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Programa de Bienvenida")
        self.root.geometry("400x300")
        
        self.label = tk.Label(self.root, text="SPARK STACK", font=("Arial", 16))
        self.label.pack(pady=50)
        
        self.developer_label = tk.Label(self.root, text="Desarrollado por: Massielle Coti (202031873)", font=("Arial", 12))
        self.developer_label.pack(pady=20)
        
        self.countdown_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.countdown_label.pack(pady=20)
        
        self.countdown(5)  # Inicia la cuenta regresiva de 5 segundos
        
        self.root.mainloop()
    
    def countdown(self, remaining):
        if remaining <= 0:
            self.root.destroy()  # Cierra la ventana de bienvenida
            self.show_main_menu()  # Muestra el menú principal
        else:
            self.countdown_label.config(text="Cuenta regresiva: " + str(remaining))
            self.root.after(1000, self.countdown, remaining - 1)  # Llama a la función después de 1 segundo
    
    def show_main_menu(self):
        main_menu = tk.Tk()
        main_menu.title("Menú Principal")
        main_menu.geometry("4000x3000")
        
        # Aquí puedes agregar los elementos del menú principal
        
        label = tk.Label(main_menu, text="¡Bienvenido al menú principal!", font=("Arial", 16))
        label.pack(pady=50)
        tk.Label(main_menu, text="PROYECTO 2", bg="#B291E8").pack(expand=True)
        tk.Button(
            main_menu,
            text="Modulo Gramatica Libre de Contexto",
            width=100,
            height=5,
            command=self.abrir_ventanaGramaticasLC,
        ).pack(expand=True)
        
        tk.Button(
            main_menu,
            text="Modulo Automata de Pila",
            width=100,
            height=5,
            command=self.abrir_ventanaAutomataPila
        ).pack(expand=True)
        
        tk.Button(
            main_menu, text="Salir", width=100, height=5, command=exit
        ).pack(expand=True)
        
        main_menu.mainloop()
        
    def abrir_ventanaGramaticasLC(self):
        ventanaG = PantallaGramaticasLC(self)
        ventanaG.grab_set()
    
    def abrir_ventanaAutomataPila(self):
        ventanaAP = PantallaAutomataPila(self)
        ventanaAP.grab_set()
        
if __name__ == "__main__":
    app = App()