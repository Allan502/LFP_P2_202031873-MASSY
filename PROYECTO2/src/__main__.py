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
        self.main_menu = tk.Tk()
        self.main_menu.title("Menú Principal")
        self.main_menu.geometry("4000x3000")
        
        # Aquí puedes agregar los elementos del menú principal
        
        label = tk.Label(self.main_menu, text="¡Bienvenido al menú principal!", font=("Arial", 16))
        label.pack(pady=50)
        tk.Label(self.main_menu, text="PROYECTO 2", bg="#B291E8").pack(expand=True)
        tk.Button(
            self.main_menu,
            text="Modulo Gramatica Libre de Contexto",
            width=100,
            height=5,
            command=self.abrir_ventanaGramaticasLC,
        ).pack(expand=True)
        
        tk.Button(
            self.main_menu,
            text="Modulo Automata de Pila",
            width=100,
            height=5,
            command=self.abrir_ventanaAutomataPila
        ).pack(expand=True)
        
        tk.Button(
            self.main_menu, text="Salir", width=100, height=5, command=self.mostrar_pantalla_salida
        ).pack(expand=True)
        
        self.label_temporizador = tk.Label(self.main_menu, text="Temporizador en la pantalla de inicio")
        self.label_temporizador.pack()
        
        self.main_menu.mainloop()
        
    def abrir_ventanaGramaticasLC(self):
        ventanaG = PantallaGramaticasLC(self)
        ventanaG.grab_set()
    
    def abrir_ventanaAutomataPila(self):
        ventanaAP = PantallaAutomataPila(self)
        ventanaAP.grab_set()
        
    def mostrar_pantalla_salida(self):
        self.main_menu.withdraw()  # Oculta la ventana principal

        self.pantalla_salida = tk.Toplevel(self.main_menu)
        self.pantalla_salida.title("Pantalla de salida")
        self.pantalla_salida.geometry("400x300")

        self.label_temporizador = tk.Label(self.pantalla_salida, text="Cerrando en:")
        self.label_temporizador.pack()

        self.label_segundos = tk.Label(self.pantalla_salida, text="")
        self.label_segundos.pack()

        self.actualizar_temporizador(5)

    def actualizar_temporizador(self, segundos):
        if segundos > 0:
            self.label_segundos.config(text=str(segundos))
            segundos -= 1
            self.label_segundos.after(1000, lambda: self.actualizar_temporizador(segundos))
        else:
            self.main_menu.destroy()  # Cierra la ventana principal y termina la aplicación
        
if __name__ == "__main__":
    app = App()