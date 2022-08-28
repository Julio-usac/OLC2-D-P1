from parser.entorno.Tipos import DataType
from parser.nodos.Nodo import Nodo

class Funcioncadena(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
       
       
        if self.hojas[1].nombre=="to_owned" or self.hojas[1].nombre=="to_string":
            self.tipo= DataType.cadena
            self.hojas[0].ejecutar(entorno)
            self.valor= self.hojas[0].valor

        elif self.hojas[1].nombre=="abs":
            self.hojas[0].ejecutar(entorno)
            self.tipo=self.hojas[0].tipo
            self.valor= abs(self.hojas[0].valor)
        
        elif self.hojas[1].nombre=="sqrt":
            self.hojas[0].ejecutar(entorno)
            self.tipo=self.hojas[0].tipo
            
            self.valor= int(self.hojas[0].valor**0.5)

        elif self.hojas[1].nombre=="clone":
            self.hojas[0].ejecutar(entorno)
            self.tipo=self.hojas[0].tipo
            self.valor= self.hojas[0].valor

        elif self.hojas[1].nombre=="-":
            self.hojas[0].ejecutar(entorno)
            self.tipo=self.hojas[0].tipo
            self.valor= self.hojas[0].valor* -1