from parser.nodos.Nodo import Nodo

class InstruccionPrint(Nodo):
    def __init__(self, token, id_nodo):
        super().__init__(token, id_nodo)

    def ejecutar(self, entorno):
        pvar=""
        cont2=0
        cont3=1
        

        for hoja in self.hojas[1].hojas[0].hojas[0].hojas:

            if hoja.nombre=="{}":
                cont2=cont3
                for hoja2 in self.hojas[1].hojas:

                    if cont2>0:
                        cont2-=1
                        continue
                    else:
                        cont3+=1
                        hoja2.ejecutar(entorno)
                        pvar+=str(hoja2.valor)
                        break
            else:
                pvar+=hoja.nombre
                
        print(pvar)
        '''self.hojas[1].ejecutar(entorno)
        print(self.hojas[1].valor)'''
        

