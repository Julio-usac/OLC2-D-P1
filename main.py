from parser.gramatica2 import parser
from parser.entorno.Entorno import Entorno

f = open("./entrada2.txt", "r")
input = f.read()
print(input)
raiz = parser.parse(input)

print(raiz.obtener_dot())
raiz.ejecutar(Entorno("Global"))