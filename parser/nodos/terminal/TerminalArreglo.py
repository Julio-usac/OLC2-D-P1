from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class TerminalArreglo(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.tipo=DataType.arreglo
        
    def ejecutar(self, entorno):
    
        pvar=[]
    
        
        for hoja2 in self.hojas[0].hojas:
            hoja2.ejecutar(entorno)
            pvar.append(hoja2.valor)

        self.valor=pvar
        