from parser.nodos.Nodo import Nodo

class InstruccionTrans(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.trans= self.nombre
    def ejecutar(self, entorno):
        if len(self.hojas)>0:
            self.hojas[0].ejecutar(entorno)
            self.tipo=self.hojas[0].tipo
            self.valor=self.hojas[0].valor
        pass
        

