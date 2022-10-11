from .C3DUtilidades import posicionHeap
class TablaSimbolosC3D():
    def __init__(self, nombre):
        self.no_entorno = 0         # Identificador de entornos (para identificar cada if, por ejemplo)
        self.entornos = {}          # Diccionario de entornos (para que la búsqueda de entorno sea fácil)
        self.nombre_entornos = []   # Nombre del entorno en formato array
        self.str_entorno = nombre   # Nombre del entorno en formato string
        self.nombre_entornos.append(nombre)
        self.contador_stack = -1    # Contador de stack
        self.contador_heap = -1     # Contador de heap

    def reset_heap(self):
        self.contador_heap = -1

    def reset_stack(self):
        self.contador_stack = -1

    def agregar_entornoC3D(self, nombre):
        nombre = nombre + str(self.no_entorno)      # Se concatena el identificador único
        self.nombre_entornos.append(nombre)         # Se agrega al entorno actual
        self.str_entorno = str(self.nombre_entornos) # Se convierte a string
        self.no_entorno += 1                        # Aumenta el id de entorno

    def agregar_entorno(self, nombre, tipoDato, tipoSimbolo):
        nombre = nombre + str(self.no_entorno)      # Se concatena el identificador único
        self.nombre_entornos.append(nombre)         # Se agrega al entorno actual
        self.str_entorno = str(self.nombre_entornos) # Se convierte a string
        nuevo_entorno = {
            'simbolos': {},
            'tam': 0,
            'tipoDato': tipoDato,
            'tipoSimbolo': tipoSimbolo
        }
        self.entornos[self.str_entorno] = nuevo_entorno # Agrega el entorno al diccionario
        self.no_entorno += 1                        # Aumenta el id de entorno

    def eliminar_entorno(self):
        self.nombre_entornos.pop()                  # Quita el nombre del entorno
        self.str_entorno = str(self.nombre_entornos)# Convierte el nombre del entorno a string

    def asignar_tam_funcion(self):
        tam = len(self.entornos[self.str_entorno]['simbolos'])
        self.entornos[self.str_entorno]['tam'] = tam

    def agregar_simbolo(self, identificador, tipoDato, tipoSimbolo, tam):
        self.contador_heap = -1
        self.contador_stack = self.contador_stack + 1
        self.entornos[self.str_entorno]['simbolos'][identificador] = {
            'identificador': identificador,
            'tipoDato': tipoDato,
            'tipoSimbolo': tipoSimbolo,
            'tam': tam,
            'posicionStack': self.contador_stack,
            'posicionHeap': self.contador_heap
        }

    def buscar_posicion(self, nombre):
        return self.entornos.get(self.str_entorno)['simbolos'].get(nombre)