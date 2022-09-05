from parser.gramatica2 import parser
from parser.entorno.Entorno import Entorno
from graphviz import Source


f = open("./Basicos.rs", "r")
input = f.read()
print(input)
raiz = parser.parse(input)



#print(raiz.obtener_dot())
entorno = Entorno("Cualquier cosa")
raiz.ejecutar(entorno)


#print("Entorno Global", entorno.tabla_simbolos)


inicio="digraph G { \n"
inicio+= "node[shape=plaintext, color=blue] \n "
inicio+= "struct1 [label=<\n"
inicio+= "<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">\n"
inicio+= "<TR><TD><b>ID</b></TD><TD><b>Tipo de simbolo</b></TD><TD><b>Tipo de dato</b></TD><TD><b>Ambito</b></TD><TD><b>Fila</b></TD></TR>\n"
for i in entorno.tabla_simbolos:
    
    inicio+= "<TR><TD>"+i+"</TD><TD>"+str(entorno.tabla_simbolos[i]["tsimbolo"])+"</TD><TD>"+str(entorno.tabla_simbolos[i]["tipo"])+"</TD><TD>"+str(entorno.tabla_simbolos[i]["ambito"])+"</TD><TD>"+str(entorno.tabla_simbolos[i]["linea"])+"</TD></TR>\n"
inicio+= "</TABLE>>];}"

s = Source(inicio, filename="arbol", format="png")
s.view()