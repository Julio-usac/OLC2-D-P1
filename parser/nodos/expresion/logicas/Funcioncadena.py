from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class Funcioncadena(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
       
       self.tipo= DataType.cadena
       self.hojas[0].ejecutar(entorno)
       self.valor= self.hojas[0].valor