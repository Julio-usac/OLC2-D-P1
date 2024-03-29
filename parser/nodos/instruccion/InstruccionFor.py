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
            ne.agregarVariable(self.hojas[0].nombre, var, DataType.int64, "local", "Variable","1")

            self.hojas[2].ejecutar(ne)
            if self.hojas[2].trans=="break":
                break
            elif self.hojas[2].trans=="continue":
                continue
            #print("Entorno de while", ne.tabla_simbolos)
                
        return

    def crear_codigo3d(self, tabla_simbolos):
        
        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
