from parser.nodos.Nodo import Nodo
from parser.entorno.Tipos import DataType

class NodoPow(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        self.hojas[0].ejecutar(entorno)
        self.hojas[1].ejecutar(entorno)

        if self.nombre=="pow":
            self.tipo=DataType.int64
            self.valor = int(self.hojas[0].valor ** self.hojas[1].valor)
        elif self.nombre=="powf":
            self.tipo=DataType.f64
            self.valor = round(self.hojas[0].valor ** self.hojas[1].valor,1)
            