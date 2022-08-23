from parser.nodos.Nodo import Nodo

class InstruccionAsignacion(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # a = expresion
        self.hojas[2].ejecutar(entorno)
        entorno.agregarVariable(self.hojas[0].nombre, self.hojas[2].valor, self.hojas[2].tipo)
        #print("El valor de ", self.hojas[0].nombre, " es", self.hojas[2].valor)
        #print(entorno.tabla_simbolos)

