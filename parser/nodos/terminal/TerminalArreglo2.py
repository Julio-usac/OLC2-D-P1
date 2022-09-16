from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class TerminalArreglo2(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.tipo=DataType.arreglo
        
    def ejecutar(self, entorno):
        self.hojas[0].ejecutar(entorno)
       
        cont=0
        valor=0
        for i in   self.hojas[1].hojas:

            i.ejecutar(entorno)
            if cont==0:
                cont=1
                valor=self.hojas[0].valor[i.valor]
            else:
                valor=valor[i.valor]

        self.valor=valor
        
        if type(valor)== list:
            self.tipo=DataType.arreglo
        elif type(valor)== int:
            self.tipo=DataType.int64
        elif type(valor)== str:
            self.tipo=DataType.cadena
        elif type(valor)== float:
            self.tipo=DataType.f64
