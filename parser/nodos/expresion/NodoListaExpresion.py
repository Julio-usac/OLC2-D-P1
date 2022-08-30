from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class NodoListaExpresion(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)
        self.nombre = "listaexp"


    def ejecutar(self, entorno):
        self.tipo = None
        arreglo = [] # [1,2,3,4,a,c,e,d]
        for hoja in self.hojas:
            hoja.ejecutar(entorno)
            arreglo.append(hoja.valor)
            if self.tipo is None:
                self.tipo = hoja.tipo
            else:
                if self.tipo != hoja.tipo:
                    self.tipo = DataType.error

        if self.tipo != DataType.error:
            self.valor = {
                'tipo': DataType.vector,
                'tipo_elementos': self.tipo,
                'valor': arreglo,
                'tam': len(arreglo)
            }
            self.tipo = DataType.vector