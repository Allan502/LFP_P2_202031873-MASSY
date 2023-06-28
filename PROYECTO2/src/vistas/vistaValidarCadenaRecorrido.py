import tkinter as tk
import tkinter.messagebox as mbox
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from PIL import ImageTk, Image
import os

class PantallaValidarCadenaRecorrido(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent, automataAFD):
        super().__init__()
        self.pantallaParent=parent
        #self.automataAFN=parent.pantallaParent.pantallaParent.pantallaParent.automatasCargadosAFN
        self.automata=automataAFD
        self.geometry("640x480")
        self.title("Pantalla de Evaluar Cadena Automata de Pila")
        self.cadena=tk.Entry(self)
        self.cadena.pack(expand=True)
        tk.Button(self, text="Recorrido Paso a Paso", width=100,height=5, command=self.ruta).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()
        
    def mostrarRuta(self):
        texto = list(self.cadena.get())
        estado_actual = self.automata[4] #el estado actual comienza con el estado inicial
        estado_anterior=[]
        pila=[]
        accept=False #aceptar cadena
        automataSeleccionado=self.automata
        w, h = A4
        pdf = canvas.Canvas("ReporteAPPaso.pdf", pagesize=A4)
        pdf.setTitle("Reporte de Automata de Pila Recorrido Paso a Paso")
        text = pdf.beginText(50, h-50)
        text.setFont("Times-Roman", 12)
        text.textLine("Nombre:"+automataSeleccionado[0])
        text.textLine("Alfabeto: "+str(automataSeleccionado[1]))
        text.textLine("Alfabeto de Pila: "+str(automataSeleccionado[2]))
        text.textLine("Estados: "+str(automataSeleccionado[3]))
        text.textLine("Estado Inicial: "+str(automataSeleccionado[4]))
        text.textLine("Estado de Aceptacion: "+str(automataSeleccionado[5]))
        text.textLine("Recorrido Paso a Paso: ")
        text.textLine()
        
        print(".......START.........")
        for simbolo in texto:
            print("Entra")
            print(estado_actual)
            print(self.automata[3])
            if estado_actual not in self.automata[3]:
                return False #El estado actual no se encuentra en los estados posibles
            
            if simbolo not in self.automata[2]: #luego verifica si esta dentro del alfabeto
                return False #La cadena se encuentra fuera del alfabeto establecido
            

            end=True #finalizar
            for transicion in self.automata[6]:
                print("entra transiciones")
                print("transicion actual")
                print(transicion)
                print("estado actual:")
                print(estado_actual)
                print("simbolo actual:")
                print(simbolo)
                if estado_actual == transicion[0]:
                    if transicion[1] == "$":
                        estado_actual=transicion[3]
                        if transicion[2] != "$":
                            if pila.__len__()== 0:
                                #aqui revisa que la pila no este vacia
                                print("la pila esta vacia cuando no deberia")
                                text.textLine("la pila esta vacia cuando no deberia")
                                return False
                            if transicion[2] == pila[-1]:
                                pila.pop()
                                #aqui se usa el metodo POP para sacar de la pila si hay algo que sacar
                                print("te saco "+transicion[2])
                                text.textLine("Se saca de la pila: "+str(transicion[2]))
                            else:
                                #aca revisa que el valor a extraer corresponda conel valor en la pila (porque no puede sacar algo que no exista)
                                print("el valor a extraer :"+transicion[2]+ " no coincide con el valor en la pila: "+pila[-1])
                                text.textLine("El valor a extraer :"+str(transicion[2])+ " no coincide con el valor en la pila: "+str(pila[-1]))
                                return False
                        else:
                            #aqui saca epsilon de la pila 
                            print("se saco $")
                            text.textLine("Se saco $ de la pila")
                        if transicion[4] != "$":
                            pila.append(transicion[4]) 
                            #aqui coloca el valor siguiente en la pila
                            print("se puso: "+transicion[4])
                            text.textLine("Se puso en la pila: "+str(transicion[4]))
                        else:
                            #aqui agrega epsilon a la pila
                            print("se puso $")
                            text.textLine("Se puso $ en la pila")
                        #aqui se mueve de transicion con epsilon
                        print("me movi con $ de "+transicion[0]+" a "+transicion[3])
                        text.textLine("Me movi con $ de "+str(transicion[0])+" a "+str(transicion[3]))
                        continue
                    else:
                        if simbolo == transicion[1]:
                            estado_actual = transicion[3]
                            if transicion[2] != "$":
                                if pila.__len__()== 0:
                                    #aqui vuelve a revisar que la pila no este vacia
                                    print("la pila esta vacia cuando no deberia")
                                    text.textLine("La pila esta vacia cuando no deberia")
                                    return False
                                if transicion[2] == pila[-1]:
                                    pila.pop()
                                    #aqui usa el metodo POP para sacar de la pila
                                    print("te saco "+transicion[2])
                                    text.textLine("Se saca de la pila: "+str(transicion[2]))
                                else:
                                    #aqui vuelve a revisar que el valor a extraer coincide con el valor en la pila
                                    print("el valor a extraer :"+transicion[2]+ " no coincide con el valor en la pila: "+pila[-1])
                                    text.textLine("El valor a extraer es: "+str(transicion[2])+ " no coincide con el valor en la pila: "+str(pila[-1]))
                                    return False
                            else:
                                #aqui se extrae epsilon
                                print("se saco $")
                                text.textLine("Se saco de la pila $")
                            if transicion[4] != "$":
                                pila.append(transicion[4]) 
                                #aqui se agrega el siguiente valor a la pila
                                print("se puso: "+transicion[4])
                                text.textLine("Se puso: "+str(transicion[4]))
                            else:
                                #aqui se agrega epsilon a la pila
                                print("se puso $")
                                text.textLine("Se puso $ en la pila")
                            #aqui continua moviendose entre transiciones
                            print("me movi con "+simbolo+" de "+transicion[0]+" a "+transicion[3])
                            text.textLine("Me movi con "+str(simbolo)+" de "+str(transicion[0])+" a "+str(transicion[3]))
                            break
                        else:
                            continue
                else:
                    continue

        for transicion in self.automata[6]:
            print("entra transiciones")
            print("transicion actual")
            print(transicion)
            print("estado actual:")
            print(estado_actual)
            print("simbolo actual:")
            print(simbolo)
            if estado_actual == transicion[0]:
                if transicion[1] == "$":
                    estado_actual=transicion[3]
                    if transicion[2] != "$":
                        if pila.__len__()== 0:
                            #aqui verifica nuevamente que la pila no este vacia
                            print("la pila esta vacia cuando no deberia")
                            text.textLine("La pila esta vacia cuando no deberia")
                            return False
                        if transicion[2] == pila[-1]:
                            pila.pop()
                            #aqui vuelve a usar POP para sacar de la pila
                            print("te saco "+transicion[2])
                            text.textLine("Se saco de la pila: "+str(transicion[2]))
                        else:
                            #aqui revisa que el valor a extraer exista dentro de la pila
                            print("el valor a extraer :"+transicion[2]+ " no coincide con el valor en la pila: "+pila[-1])
                            text.textLine("El valor a extraer: "+str(transicion[2])+ " no coincide con el valor en la pila "+str(pila[-1]))
                            return False
                    else:
                        #aqui saca epsilon
                        print("se saco $")
                        text.textLine("Se saco $ de la pila")
                    if transicion[4] != "$":
                        pila.append(transicion[4]) 
                        #aqui agrega a la pila usando APPEND
                        print("se puso: "+transicion[4])
                        text.textLine("Se puso en la pila: "+str(transicion[4]))
                    else:
                        #aqui agrega a la pila epsilon
                        print("se puso $")
                        text.textLine("Se puso $ en la pila")
                    #aqui continua moviendose entre transiciones
                    print("me movi con $ de "+transicion[0]+" a "+transicion[3])
                    text.textLine("Me movi con $ de "+str(transicion[0])+" a "+str(transicion[3]))
                    continue
            else:
                continue
        #aqui solo muestro el estado final
        print("Estado final: "+estado_actual)
        text.textLine("Estado final: "+str(estado_actual))
        if pila.__len__()>0:
            #aqui revisa si la cadena se vacio, y si no entonces es invalida
            print("cadena invalida, la pila no esta vacia")
            text.textLine("Cadena invalida, la pila no esta vacia")
        if estado_actual in self.automata[5]:
            print("cadena valida")
            #aqui llega si la cadena es valida y lo muestra en pantalla
            text.textLine("CADENA VALIDA")
            text.textLine()
            text.textLine("Automata de Pila generado con Graphviz")
            pdf.drawText(text)
            pdf.drawInlineImage("output/"+automataSeleccionado[0]+".png", 300,h-400, width=200, height=200, preserveAspectRatio=True)
            pdf.save()
            webbrowser.open_new_tab('ReporteAPPaso.pdf')
            return True
        else:
            #aqui manda un mensaje al usuario explicando que la cadena no es valida y por eso no la puede recorrer
            print("cadena invalida")
            mbox.showinfo("Mensaje", "LA CADENA ES INVALIDA, por lo que no se puede generar recorrido paso a paso")
            return False
        
    def ruta(self):
        # Realizar las validaciones necesarias
        if self.mostrarRuta():
            tk.Label(self, text="Cadena valida").pack(expand=True)
        else:
            tk.Label(self, text="Cadena invalida").pack(expand=True)
            