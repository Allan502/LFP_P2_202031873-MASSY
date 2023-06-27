class Datos:
    def __init__(self, nombre, apellido, nombreCurso, seccion, carnet, cui):
        self.nombre = nombre
        self.apellido = apellido
        self.nombreCurso = nombreCurso
        self.seccion = seccion
        self.carnet = carnet
        self.cui = cui

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.nombreCurso} Seccion: {self.seccion} Carnet: {self.carnet} Cui: {self.cui}" 