from parser.nodos.Nodo import Nodo

class NodoExpresion(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        self.hojas[0].ejecutar(entorno)
        self.copiar_valorhoja(0)
        self.es_expresion = True