from parser.nodos.Nodo import Nodo
from parser.entorno.Tipos import *

class TerminalDecimal(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.nombre = self.valor
        self.tipo = DataType.f64

    def ejecutar(self, entorno):
        pass