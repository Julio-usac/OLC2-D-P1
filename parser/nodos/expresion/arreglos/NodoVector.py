from parser.nodos.Nodo import Nodo

class NodoVector(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # vec! [ listaexp ]
        self.hojas[2].ejecutar(entorno) # listaexp
        self.tipo = self.hojas[2].tipo # valor de tipoexp
        self.valor = self.hojas[2].valor
