from parser.nodos.Nodo import Nodo
from parser.entorno.Tipos import *
class TerminalChar(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.nombre = self.valor
        self.tipo = DataType.char

    def ejecutar(self, entorno):
        pass