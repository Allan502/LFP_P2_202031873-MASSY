class DataGramatica():
    def __init__(self):
        self.noTerminales = []
        self.terminales = []
        self.noTerminalInicial=None
        self.producciones=[]

class ProduccionesGramatica():
    def __init__(self, noTerminales, terminales):
        self.noTerminales = noTerminales
        self.terminales = terminales
