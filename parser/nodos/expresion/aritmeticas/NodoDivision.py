from parser.nodos.Nodo import Nodo
from parser.entorno.Tipos import DataType

class NodoDivision(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # exp / exp
        self.hojas[0].ejecutar(entorno)
        self.hojas[2].ejecutar(entorno)
        self.validar_tipo('/', self.hojas[0].tipo, self.hojas[2].tipo)
        if self.tipo==DataType.f64:

            self.valor = round(self.hojas[0].valor / self.hojas[2].valor,1)
        elif self.tipo==DataType.int64:
            self.valor = int(self.hojas[0].valor / self.hojas[2].valor)