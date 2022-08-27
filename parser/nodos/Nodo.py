from abc import ABC, abstractmethod
from ..entorno.Tipos import *


class Nodo(ABC):
    def __init__(self, token, id_nodo):
        self.nombre = token.type
        self.tipo = token.type
        self.valor = token.value
        self.id_nodo = id_nodo
        self.hojas = []
        self.es_expresion = False
        super().__init__()

    def obtener_dot(self):
        texto = "nodo{0}[label=\"{1}\"];".format(self.id_nodo, self.nombre)
        if len(self.hojas) > 0:
            texto += "nodo{0}->{{".format(self.id_nodo)
            texto2 = ""
            for x in range(0, len(self.hojas)):
                if x != 0:
                    texto += ","
                texto += "nodo{0}".format(self.hojas[x].id_nodo)
                texto2 += self.hojas[x].obtener_dot()
            texto += "};"
            texto += texto2
        return texto

    def validar_tipo(self, operador, tipo1, tipo2):
        result = validador.get(operador, DataType.error)
        if result == DataType.error:
            self.tipo = result
            return
        result2 = result.get(tipo1, DataType.error)
        if result2 == DataType.error:
            self.tipo = result2
            return
        if tipo1==tipo2 and result2.get(tipo2, DataType.error)!=DataType.cadena:

            self.tipo = result2.get(tipo2, DataType.error)

        elif result2.get(tipo2, DataType.error)==DataType.cadena:
            self.tipo=result2.get(tipo2, DataType.error)

    def copiar_valorhoja(self, nohoja):
        if nohoja < len(self.hojas):
            self.valor = self.hojas[nohoja].valor
            self.tipo = self.hojas[nohoja].tipo
            
    @abstractmethod
    def ejecutar(self, entorno):
        pass
