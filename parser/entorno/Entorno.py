class Entorno():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tabla_simbolos = {}
        self.entorno_anterior = None

    def agregarVariable(self, nombre_variable, simbolo):
        # Validaciones
        self.tabla_simbolos[nombre_variable] = simbolo


