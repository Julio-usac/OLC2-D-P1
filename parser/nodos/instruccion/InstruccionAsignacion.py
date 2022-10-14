from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class InstruccionAsignacion(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # a = expresion
        self.hojas[2].ejecutar(entorno)
        var= "Variable"
        if self.hojas[2].tipo== DataType.arreglo:
            var="Arreglo"
        entorno.agregarVariable(self.hojas[0].nombre, self.hojas[2].valor, self.hojas[2].tipo,"Global",var,self.linea)


    def crear_codigo3d(self, tabla_simbolos):
        # a = expresion
        self.hojas[2].crear_codigo3d(tabla_simbolos)
        posicionStack = tabla_simbolos.buscar_posicion(self.hojas[0].nombre)['posicionStack']
        texto = self.hojas[2].expresion + "\n"
        self.referencia = self.obtener_temporal()
        texto += str(self.referencia) + " = P + " + str(posicionStack) + "\n"
        texto += "stack[(int)" + str(self.referencia) + "]" + " = " + str(self.hojas[2].referencia) + "\n"
        self.expresion = texto