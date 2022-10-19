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

    
    def crear_codigo3d(self, tabla_simbolos):
        # a = expresion
        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
        self.expresion = texto