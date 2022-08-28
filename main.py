from parser.gramatica2 import parser
from parser.entorno.Entorno import Entorno

f = open("./entrada3.rs", "r")
input = f.read()
print(input)
raiz = parser.parse(input)

print(raiz.obtener_dot())
entorno = Entorno("Cualquier cosa")
raiz.ejecutar(entorno)
print("Entorno Global", entorno.tabla_simbolos)

