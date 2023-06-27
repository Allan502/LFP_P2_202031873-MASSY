class DataAutomataPila():
    def __init__(self):
        self.alfabeto = []
        self.simbolosPila=[]
        self.estados = []
        self.estadoInicial = None
        self.estadoAceptacion=None
        self.transiciones=[]

class TransicionesAutomataPila():
    def __init__(self, estadoOrigen, simboloEntrada, simboloExtraePila, estadoDestino, simboloInsertaPila):
        self.estadoOrigen = estadoOrigen
        self.simboloEntrada = simboloEntrada
        self.simboloExtraePila = simboloExtraePila
        self.estadoDestino = estadoDestino
        self.simboloInsertaPila = simboloInsertaPila
    def transform(self):
        return [self.estadoOrigen,self.simboloEntrada,self.simboloExtraePila,self.estadoDestino,self.simboloInsertaPila]
    