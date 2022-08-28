from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionElse(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # else { instrucciones }

        ne = Entorno("entornoelse")
        ne.asignarAnterior(entorno)
        self.hojas[2].ejecutar(ne)
        self.trans=self.hojas[2].trans
        self.copiar_valorhoja(2)
        #print("Entorno de else", ne.tabla_simbolos)
        return


