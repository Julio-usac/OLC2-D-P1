from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo


class NodoAccesoVector(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        # identificador listexp
        self.hojas[0].ejecutar(entorno)
        if self.hojas[0].valor is not None:
            if self.hojas[0].tipo == DataType.vector:
                self.hojas[1].ejecutar(entorno)
                # El valor es un arreglo y el tipo de los arreglos es lo que se valida
                if self.hojas[1].valor['tipo_elementos'] == DataType.int64:
                    vector = self.hojas[0].valor
                    # vector base(tabla de simbolos) vector = [1,2]
                    for pos in self.hojas[1].valor['valor']: # posicion = 2 [2] posiciones (indices)
                        if vector['tipo'] == DataType.vector:
                            if pos < len(vector):
                                vector = vector['valor'][pos]
                            else:
                                print("Fuera de rango")
                        else:
                            print("Error")
                    self.valor = vector
                else:
                    print("Error en los accesos a posición")
            else:
                print("La variable", self.hojas[0].nombre, "no es un vector")
        else:
            print("La variable", self.hojas[0].nombre, "no existe")