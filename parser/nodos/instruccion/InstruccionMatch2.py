from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionMatch2(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        
        self.hojas[0].ejecutar(entorno)


        estado=False
        for hoja in self.hojas[1].hojas:

            for hoja2 in hoja.hojas[0].hojas:
                hoja2.ejecutar(entorno)
                if hoja2.valor==self.hojas[0].valor:
                    ne = Entorno("entornomatch")
                    ne.asignarAnterior(entorno)
                    hoja.hojas[1].ejecutar(ne)
                    estado= True
                    break
        
        if estado!=True :
            ne = Entorno("entornomatch")
            ne.asignarAnterior(entorno)
            self.hojas[1].hojas[len(self.hojas[1].hojas)-1].hojas[1].ejecutar(ne)


        
        return

