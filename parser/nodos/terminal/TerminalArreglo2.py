from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class TerminalArreglo2(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.tipo=DataType.arreglo
        
    def ejecutar(self, entorno):
        self.hojas[0].ejecutar(entorno)
        self.hojas[1].ejecutar(entorno)
        
        self.valor=self.hojas[0].valor[self.hojas[1].valor]
    
        self.tipo=DataType.int64