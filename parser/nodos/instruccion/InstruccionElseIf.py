from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionElseIf(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # else if expresion { instrucciones }
        # else if expresion { instrucciones } else/elseif
        self.hojas[2].ejecutar(entorno)
        if self.hojas[2].tipo == DataType.boolean:
            if self.hojas[2].valor:

                # instrucciones
                ne = Entorno("entornoif")
                ne.asignarAnterior(entorno)
                self.hojas[4].ejecutar(ne)
                self.copiar_valorhoja(4)
                print("Entorno de elseif", ne.tabla_simbolos)
                return
            else:
                if len(self.hojas) == 7:
                    self.hojas[6].ejecutar(entorno)
                    self.copiar_valorhoja(6)
                return
        print('El tipo de dato debe ser booleano ')
