from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class InstruccionAsignacion2(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # a = expresion
        self.hojas[2].ejecutar(entorno)

        

     
        valor=entorno.tabla_simbolos[self.hojas[0].nombre]["valor"]
        cont=len(self.hojas[3].hojas)
        for i in  self.hojas[3].hojas:

            i.ejecutar(entorno)
            if cont>1:
                cont-=1
                valor=valor[i.valor]
            else:
                valor[i.valor]=self.hojas[2].valor


