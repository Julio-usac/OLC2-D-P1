class Entorno():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tabla_simbolos = {}
        self.entorno_anterior = None

    def agregarVariable(self, nombre_variable, valor, tipo):
        # Validaciones
        simbolo = {'valor': valor, 'tipo': tipo}
        self.tabla_simbolos[nombre_variable] = simbolo

    def asignarAnterior(self, anterior):
        self.entorno_anterior = anterior

    def obtenerValor(self, nombre):
        simbolo = self.tabla_simbolos.get(nombre, None)
        if simbolo != None:
            return simbolo
        tmp_anterior = self.entorno_anterior
        while tmp_anterior != None:
            simbolo = tmp_anterior.tabla_simbolos.get(nombre, None)
            if simbolo != None:
                return simbolo
        return None
