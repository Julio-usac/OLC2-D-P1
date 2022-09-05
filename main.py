from parser.gramatica2 import parser
from parser.entorno.Entorno import Entorno
from graphviz import Source





entorno = Entorno("Entorno")
while True:
    numero = int(input("Elija una opcion: \n 1. Correr archivo \n 2.Generar tabla de simbolos \n 3.Salir \n" ))
    if numero==3:
        break;
    elif numero==1:

        f = open("./Basicos.rs", "r")
        lectura = ""

        for i in f:
            lectura=lectura+ i + "\n"

        #input = f.read()

        #print(input)
        raiz = parser.parse(lectura)



        #print(raiz.obtener_dot())
        
        raiz.ejecutar(entorno)

    elif numero==2:
        

        inicio="digraph G { \n"
        inicio+= "node[shape=plaintext, color=blue] \n "
        inicio+= "struct1 [label=<\n"
        inicio+= "<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">\n"
        inicio+= "<TR><TD><b>ID</b></TD><TD><b>Tipo de simbolo</b></TD><TD><b>Tipo de dato</b></TD><TD><b>Ambito</b></TD><TD><b>Fila</b></TD></TR>\n"
        for i in entorno.tabla_simbolos:
            
            inicio+= "<TR><TD>"+i+"</TD><TD>"+str(entorno.tabla_simbolos[i]["tsimbolo"])+"</TD><TD>"+str(entorno.tabla_simbolos[i]["tipo"])+"</TD><TD>"+str(entorno.tabla_simbolos[i]["ambito"])+"</TD><TD>"+str(entorno.tabla_simbolos[i]["linea"])+"</TD></TR>\n"
        inicio+= "</TABLE>>];}"

        s = Source(inicio, filename="TablaS", format="png")
        s.view()