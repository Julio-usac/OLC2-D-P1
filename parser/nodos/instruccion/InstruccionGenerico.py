from parser.nodos.Nodo import Nodo

class InstruccionGenerico(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        cont=0
        for hoja in self.hojas:
            cont+=1
            hoja.ejecutar(entorno)
            self.trans=hoja.trans
            if hoja.trans !="no":
                break
        
        self.copiar_valorhoja(cont-1)
