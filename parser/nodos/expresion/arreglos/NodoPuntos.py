from parser.nodos.Nodo import Nodo
from parser.entorno.Tipos import *

class NodoPuntos(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        self.hojas[0].ejecutar(entorno)
        self.hojas[1].ejecutar(entorno)

        cont=self.hojas[0].valor
        arr=[]
        while cont<self.hojas[1].valor:
            arr.append(cont)
            cont+=1
        
        self.valor=arr
        self.tipo= DataType.arreglo
        
        pass