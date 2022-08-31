from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionFor(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # if expresion { instrucciones }
        # if bool { instrucciones }

       
        self.hojas[0].ejecutar(entorno)
        self.hojas[1].ejecutar(entorno)

        for var in self.hojas[1].valor:
            ne = Entorno("entornofor")
            ne.asignarAnterior(entorno)
            ne.agregarVariable(self.hojas[0].nombre, var, DataType.int64)

            self.hojas[2].ejecutar(ne)
            if self.hojas[2].trans=="break":
                break
            elif self.hojas[2].trans=="continue":
                continue
            #print("Entorno de while", ne.tabla_simbolos)
                
        return

       
