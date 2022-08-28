from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionElseIf(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # else if expresion { instrucciones }
        # else if expresion { instrucciones } else/elseif
        self.hojas[0].ejecutar(entorno)
        if self.hojas[0].tipo == DataType.boolean:
            if self.hojas[0].valor:

                # instrucciones
                ne = Entorno("entornoelseif")
                ne.asignarAnterior(entorno)
                self.hojas[2].ejecutar(ne)
                self.trans=self.hojas[2].trans
                self.copiar_valorhoja(2)
                #print("Entorno de elseif", ne.tabla_simbolos)
                return
            else:
                if len(self.hojas) == 5:
                    self.hojas[4].ejecutar(entorno)
                    self.trans=self.hojas[4].trans
                    self.copiar_valorhoja(4)
                return
        print('El tipo de dato debe ser booleano ')
