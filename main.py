from parser.gramatica2 import parser
from parser.entorno.Entorno import Entorno
from graphviz import Source
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import Pimp


'''
entorno = Entorno("Entorno")
while True:
    numero = int(input("Elija una opcion: \n 1. Correr archivo \n 2.Generar tabla de simbolos \n 3.Salir \n" ))
    if numero==3:
        break;
    elif numero==1:
        Pimp.imprimir=""
        f = open("./Basicos.rs", "r")
        lectura = ""

        for i in f:
            lectura=lectura+ i + "\n"

        #input = f.read()

        #print(input)
        raiz = parser.parse(lectura)



        #print(raiz.obtener_dot())
        
        raiz.ejecutar(entorno)
        print(Pimp.imprimir)

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
'''
global entorno 
class Aplicacion:
    
    def __init__(self):
       
        self.ventana1=tk.Tk()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=100, height=20)
        self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
        self.framecopia()        
        self.scrolledtext2=st.ScrolledText(self.ventana1, width=100, height=17)
        self.scrolledtext2.grid(column=0,row=2, padx=20, pady=10)
        self.ventana1.mainloop()


    def framecopia(self):
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Opciones")
        self.labelframe1.grid(column=0, row=1, padx=5, pady=3, sticky="w")
        self.dato1=tk.StringVar()
        self.dato2=tk.StringVar()   
        self.dato3=tk.StringVar()
        self.dato4=tk.StringVar()

        

        self.boton1=ttk.Button(self.labelframe1, text="Ejecutar", command=self.Ejecutar)
        self.boton1.grid(column=1, row=4, padx=10, pady=10)

        self.boton2=ttk.Button(self.labelframe1, text="Tabla de simbolos", command=self.TablaSimbolo)
        self.boton2.grid(column=3, row=4, padx=10, pady=10)


    def Ejecutar(self):
        global entorno 
        entorno = Entorno("Entorno")
        datos=self.scrolledtext1.get("1.0", tk.END)
        raiz = parser.parse(datos)

        
        raiz.ejecutar(entorno)
        
        self.scrolledtext2.delete("1.0", tk.END)        
        self.scrolledtext2.insert("1.0", Pimp.imprimir)
        Pimp.imprimir=""
    
    def TablaSimbolo(self):
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


aplicacion1=Aplicacion() 
