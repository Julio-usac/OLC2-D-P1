from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class NodoAs(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # exp + exp
        self.hojas[0].ejecutar(entorno)
        self.hojas[2].ejecutar(entorno)
        

        if self.hojas[2].valor=="i64":
            self.valor=int(self.hojas[0].valor)
            self.tipo = DataType.int64
        elif self.hojas[2].valor=="f64":
            self.valor=float(self.hojas[0].valor)
            self.tipo = DataType.f64