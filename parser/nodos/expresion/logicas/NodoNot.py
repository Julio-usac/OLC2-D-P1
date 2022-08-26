from parser.nodos.Nodo import Nodo

class NodoNot(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # exp < exp
        self.hojas[1].ejecutar(entorno)
        self.validar_tipo('!', self.hojas[1].tipo, self.hojas[1].tipo)
        self.valor = not self.hojas[1].valor