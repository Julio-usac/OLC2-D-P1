from parser.nodos.Nodo import Nodo

class InstruccionGenerico(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        for hoja in self.hojas:
            hoja.ejecutar(entorno)
