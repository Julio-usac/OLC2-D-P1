from parser.nodos.Nodo import Nodo
from parser.entorno.Tipos import *

class TerminalBool(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.nombre = self.valor
        self.tipo = DataType.boolean

    def ejecutar(self, entorno):
        if self.valor=="true":
            self.valor=True
        elif self.valor=="false":
            self.valor=False