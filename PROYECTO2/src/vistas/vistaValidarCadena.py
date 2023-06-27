import tkinter as tk
import tkinter.messagebox as mbox

class PantallaValidarCadena(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent, automataAFD):
        super().__init__()
        self.pantallaParent=parent
        #self.automataAFN=parent.pantallaParent.pantallaParent.pantallaParent.automatasCargadosAFN
        self.automata=automataAFD
        self.geometry("640x480")
        self.title("Pantalla de Evaluar Cadena de Automata de Pila")
        self.cadena=tk.Entry(self)
        self.cadena.pack(expand=True)
        tk.Button(self, text="Validar", width=100,height=5, command=self.validar).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()

    def crear_entry(self):
        texto = list(self.cadena.get())
        estado_actual = self.automata[4] #el estado actual comienza con el estado inicial
        estado_anterior=[]
        pila=[]
        accept=False #aceptar cadena
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
                                print("la pila esta vacia cuando no deberia")
                                return False
                            if transicion[2] == pila[-1]:
                                pila.pop()
                                print("te saco "+transicion[2])
                            else:
                                print("el valor a extraer :"+transicion[2]+ " no coincide con el valor en la pila: "+pila[-1])
                                return False
                        else:
                            print("se saco $")
                        if transicion[4] != "$":
                            pila.append(transicion[4]) 
                            print("se puso: "+transicion[4])
                        else:
                            print("se puso $")
                        print("me movi con $ de "+transicion[0]+" a "+transicion[3])
                        continue
                    else:
                        if simbolo == transicion[1]:
                            estado_actual = transicion[3]
                            if transicion[2] != "$":
                                if pila.__len__()== 0:
                                    print("la pila esta vacia cuando no deberia")
                                    return False
                                if transicion[2] == pila[-1]:
                                    pila.pop()
                                    print("te saco "+transicion[2])
                                else:
                                    print("el valor a extraer :"+transicion[2]+ " no coincide con el valor en la pila: "+pila[-1])
                                    return False
                            else:
                                print("se saco $")
                            if transicion[4] != "$":
                                pila.append(transicion[4]) 
                                print("se puso: "+transicion[4])
                            else:
                                print("se puso $")
                            print("me movi con "+simbolo+" de "+transicion[0]+" a "+transicion[3])
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
                            print("la pila esta vacia cuando no deberia")
                            return False
                        if transicion[2] == pila[-1]:
                            pila.pop()
                            print("te saco "+transicion[2])
                        else:
                            print("el valor a extraer :"+transicion[2]+ " no coincide con el valor en la pila: "+pila[-1])
                            return False
                    else:
                        print("se saco $")
                    if transicion[4] != "$":
                        pila.append(transicion[4]) 
                        print("se puso: "+transicion[4])
                    else:
                        print("se puso $")
                    print("me movi con $ de "+transicion[0]+" a "+transicion[3])
                    continue
            else:
                continue

        print("Estado final: "+estado_actual)
        if pila.__len__()>0:
            print("cadena invalida, la pila no esta vacia")
        if estado_actual in self.automata[5]:
            print("cadena valida")
            return True
        else:
            print("cadena invalida")
            return False
        

    def validar(self):
        
        # Realizar las validaciones necesarias
        if self.crear_entry():
            mbox.showinfo("Cadena correcta", "Cadena valida")
        else:
            mbox.showerror("Cadena incorrecta", "Cadena invalida")
