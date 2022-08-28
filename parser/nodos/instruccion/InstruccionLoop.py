from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionLoop(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # if expresion { instrucciones }
        # if bool { instrucciones }
        while True:
            # instrucciones
            ne = Entorno("entornoLoop")
            ne.asignarAnterior(entorno)
            self.hojas[1].ejecutar(ne)
            self.copiar_valorhoja(1)
            if self.hojas[1].trans=="break":
                
                break
            elif self.hojas[1].trans=="continue":
                continue
            
            #print("Entorno de while", ne.tabla_simbolos)
            
        return

