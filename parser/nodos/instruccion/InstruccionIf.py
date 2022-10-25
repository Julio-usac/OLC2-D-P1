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
                self.trans=self.hojas[2].trans
                self.copiar_valorhoja(2)
                #print("Entorno de if", ne.tabla_simbolos)
                return
            else:
                if len(self.hojas) == 5:
                    self.hojas[4].ejecutar(entorno)
                    self.trans=self.hojas[4].trans
                    self.copiar_valorhoja(4)
            return
        
        print('El tipo de dato debe ser booleano')

    def crear_codigo3d(self, tabla_simbolos):

        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
        self.expresion = texto