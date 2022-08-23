from parser.nodos.Nodo import Nodo

class NodoResta(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # exp - exp
        self.hojas[0].ejecutar(entorno)
        self.hojas[2].ejecutar(entorno)
        self.validar_tipo('+', self.hojas[0].tipo, self.hojas[2].tipo)
        self.valor = self.hojas[0].valor - self.hojas[2].valor