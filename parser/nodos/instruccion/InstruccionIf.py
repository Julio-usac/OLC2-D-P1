from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionIf(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # if expresion { instrucciones }
        # if bool { instrucciones }
        self.hojas[0].ejecutar(entorno)
        if self.hojas[0].tipo == DataType.boolean:
            if self.hojas[0].valor:
                # instrucciones
                ne = Entorno("entornoif")
                ne.asignarAnterior(entorno)
                self.hojas[2].ejecutar(ne)
                self.copiar_valorhoja(2)
                print("Entorno de if", ne.tabla_simbolos)
                return
            else:
                if len(self.hojas) == 5:
                    self.hojas[4].ejecutar(entorno)
                    self.copiar_valorhoja(4)
                return
        
        print('El tipo de dato debe ser booleano')
