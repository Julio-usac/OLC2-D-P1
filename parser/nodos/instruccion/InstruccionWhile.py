from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionWhile(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # if expresion { instrucciones }
        # if bool { instrucciones }
        self.hojas[0].ejecutar(entorno)
        if self.hojas[0].tipo == DataType.boolean:
            while self.hojas[0].valor:
                # instrucciones
                ne = Entorno("entornowhile")
                ne.asignarAnterior(entorno)
                self.hojas[2].ejecutar(ne)
                self.hojas[0].ejecutar(entorno)
            
                if self.hojas[2].trans=="break":
                    
                    break
                elif self.hojas[2].trans=="continue":
                    continue
                
                #print("Entorno de while", ne.tabla_simbolos)
                
            return

        print('El tipo de dato debe ser booleano')
