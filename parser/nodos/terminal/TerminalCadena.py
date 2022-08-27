from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo


class TerminalCadena(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.nombre = self.valor
        self.tipo = DataType.direccion
        self.no_formatos = 0

    def ejecutar(self, entorno):
        pass

    def agregarFormato(self, id_nodo):
        self.hojas.append(TerminalParametroFormato(id_nodo))
        self.no_formatos += 1


    def agregarTexto(self, nombre, id_nodo):
        self.hojas.append(TerminalTexto(id_nodo, nombre))


class TerminalParametroFormato():
    def __init__(self, id_nodo):
        self.id_nodo = id_nodo
        self.nombre = "{}"

    def ejecutar(self):
        pass

    def obtener_dot(self):
        return "nodo{0}[label=\"{1}\"];".format(self.id_nodo, self.nombre)


class TerminalTexto():
    def __init__(self, id_nodo, nombre):
        self.id_nodo = id_nodo
        self.nombre = nombre

    def ejecutar(self):
        pass

    def obtener_dot(self):
        return "nodo{0}[label=\"{1}\"];".format(self.id_nodo, self.nombre)