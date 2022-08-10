from Analyzer.gramatica2 import parser

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)