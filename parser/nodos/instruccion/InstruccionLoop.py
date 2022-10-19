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
            elif self.hojas[1].trans=="return":
                break
            
            #print("Entorno de while", ne.tabla_simbolos)
            
        return

    def crear_codigo3d(self, tabla_simbolos):
        # a = expresion
        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
        self.expresion = texto