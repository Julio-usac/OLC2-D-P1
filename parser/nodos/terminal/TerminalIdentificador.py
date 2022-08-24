from parser.nodos.Nodo import Nodo

class TerminalIdentificador(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.nombre = self.valor

    def ejecutar(self, entorno):
        valvar = entorno.obtenerValor(self.nombre)
        if valvar != None:
            self.valor = valvar['valor']
            self.tipo = valvar['tipo']