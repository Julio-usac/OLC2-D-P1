from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo
from parser.entorno.Entorno import Entorno


class InstruccionMatch(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        
        self.hojas[0].ejecutar(entorno)
        self.hojas[1].hojas[0].hojas[0].ejecutar(entorno)

        estado=False
        for hoja in self.hojas[1].hojas:

            hoja.hojas[0].ejecutar(entorno)
            hoja.hojas[1].ejecutar(entorno)

            if hoja.hojas[0].valor==self.hojas[0].valor:
                self.valor=hoja.hojas[1].valor
                self.tipo= hoja.hojas[1].tipo
                estado=True
                break;

        if estado!=True :
            self.hojas[1].hojas[len(self.hojas[1].hojas)-1].hojas[1].ejecutar(entorno)
            self.valor=self.hojas[1].hojas[len(self.hojas[1].hojas)-1].hojas[1].valor
            self.tipo= self.hojas[1].hojas[len(self.hojas[1].hojas)-1].hojas[1].tipo

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