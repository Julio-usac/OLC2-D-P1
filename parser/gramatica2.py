from parser.nodos import *


global noNode
noNode = 0


reservadas = {
    'pub' : 'PUB',
    'loop' : 'LOOP',
    'mod': 'MODF',
    'fn' : 'FN',
    'main' : 'MAIN',
    'println' : 'PRINT',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'i64' : 'I64',
    'f64' : 'F64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'String' : 'STRING',
    'str' : 'STR',
    'usize' : 'USIZE',
    'let' : 'LET',
    'mut' : 'MUT',
    'struct' : 'STRUCT',
    'Vec' : 'VEC',
    'vec' : 'VECM',
    'pow' : 'POW',
    'powf' : 'POWF',
    'to_string' : "TOSTRING",
    'sqrt' : 'SQRT',
    'clone' : 'CLONE',
    'abs' : 'ABS',
    'if' : 'IF',
    'else' : 'ELSE',
    'match' : 'MATCH',
    'while' : 'WHILE',
    'for' : 'FOR',
    'in' : 'IN',
    'return' : 'RETURN',
    'continue' : 'CONTINUE',
    'len' : 'LEN',
    'break'  : 'BREAK',
    'to_owned' : 'TOOWNED',
    'as'  : 'AS'

}

tokens  = [
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'DECIMAL',
    'ENTERO',
    'PTCOMA',
    'FORM',
    'LLAVEIZQ',
    'LLAVEDER',
    'NOT',
    'COMA',
    'DPT',
    'MEIGUAL',
    'MAIGUAL',
    'MENOR',
    'MAYOR',
    'DIS',
    'IGUAL',
    'AND',
    'OR',
    'PT',
    'MOD',
    'AMP',
    'ID'
 ] + list(reservadas.values())

# Tokens

t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_LLAVEIZQ  = r'{'
t_LLAVEDER  = r'}'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PTCOMA    = r';'
t_COMA      = r','
t_DPT       = r':'
t_MEIGUAL   = r'<='
t_MAIGUAL   = r'>='
t_MENOR     = r'<'
t_MAYOR     = r'>'
t_DIS       = r'!='
t_NOT       = r'!'
t_IGUAL     = r'='
t_AND       = r'&&'
t_AMP       = r'&'
t_MOD       = r'%'
t_OR        = r'\|\|'
t_PT        = r'\.'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID')    # Check for reserved words
     return t
     

def t_FORM(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Quitamos las comillas
    nodoCadena = TerminalCadena(t, getNoNodo())
    estado = "S2"
    texto = ""
    for x in t.value:
        if x == "{":
            if estado == "S2":
                estado = "S3"
                continue
            elif estado == "S3":
                estado = "S2"
        elif x == "}":
            if estado == "S3":
                estado = "S2"
                nodoCadena.agregarTexto(texto, getNoNodo())
                nodoCadena.agregarFormato(getNoNodo())
                texto = ""
                continue
            else:
                estado = "ERROR"
        else:
            texto += x
    if texto != "":
        nodoCadena.agregarTexto(texto, getNoNodo())
    if estado == "S3":
        estado = "ERROR"
    if estado != "S2":
        print("Error con el formato de cadena", t.value)
        t.value = ""
        return t
    t.value = nodoCadena
    return t



# Caracteres ignorados
t_ignore = " \t"

def t_comment(t):
    r'\/\/[^\n]+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico

import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática

def p_funciones_lista(t):
    '''funciones    : funcion  funciones 
                    | funcion '''
    t[0] = InstruccionGenerico(t.slice[0], getNoNodo())
    if (len(t) == 3):
        t[0].hojas = t[2].hojas
        t[0].hojas.insert(0, t[1])
    else:
        t[0].hojas.append(t[1])
        
def p_funciones_evaluar(t):
    '''funcion  : PUB FN ID PARIZQ parametros PARDER tipofun LLAVEIZQ instrucciones LLAVEDER
                | FN ID PARIZQ parametros PARDER tipofun LLAVEIZQ instrucciones LLAVEDER
                | PUB MODF ID LLAVEIZQ funciones LLAVEDER
                | MODF ID LLAVEIZQ funciones LLAVEDER
                | FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER
                | STRUCT ID LLAVEIZQ liststruct LLAVEDER'''
    
    if t[2] == "main":
        t[0]=t[6]
        '''t[0] = InstruccionAsignacion(t.slice[0], getNoNodo())
        t[0].hojas.append(TerminalIdentificador(t.slice[3], getNoNodo()))
        t[0].hojas.append(TerminalGenerico(t.slice[5], getNoNodo()))
        t[0].hojas.append(t[6])'''

def p_parametros(t):
    '''parametros   : parametros2  
                    | empty '''

def p_parametros2(t):
    '''parametros2  : parametros2 COMA mutable ID DPT tipos
                    | mutable ID DPT tipos  '''


def p_liststruct(t):
    '''liststruct : liststruct COMA ID DPT tipos 
                | ID DPT tipos '''

def p_tipofun(t):
    '''tipofun : MENOS MAYOR tipos 
                | empty '''


def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones  
                        | instruccion '''
    t[0] = InstruccionGenerico(t.slice[0], getNoNodo())
    if (len(t) == 3):
        t[0].hojas = t[2].hojas
        t[0].hojas.insert(0, t[1])
    else:
        t[0].hojas.append(t[1])

def p_instruccion(t):
    '''instruccion  : LET mutable ID pyc arrtipos IGUAL logica PTCOMA
                    | ID listarreglo IGUAL logica PTCOMA
                    | ID PARIZQ listexpr PARDER PTCOMA
                    | PRINT NOT PARIZQ listexpr PARDER PTCOMA
                    | IF logica LLAVEIZQ instrucciones LLAVEDER unelse
                    | LOOP LLAVEIZQ instrucciones LLAVEDER
                    | BREAK logica PTCOMA
                    | BREAK PTCOMA
                    | RETURN logica PTCOMA
                    | CONTINUE PTCOMA
                    | WHILE logica LLAVEIZQ instrucciones LLAVEDER
                    | FOR ID IN opcionfor LLAVEIZQ instrucciones LLAVEDER'''
    
    if t[1] == "let":
        t.slice[0].type="Asignacion";
        t[0] = InstruccionAsignacion(t.slice[0], getNoNodo())
        t[0].hojas.append(TerminalIdentificador(t.slice[3], getNoNodo()))
        t[0].hojas.append(TerminalGenerico(t.slice[6], getNoNodo()))
        t[0].hojas.append(t[7])
    elif t[3] == "=":
        t[0] = InstruccionAsignacion(t.slice[0], getNoNodo())
        t[0].hojas.append(TerminalIdentificador(t.slice[1], getNoNodo()))
        t[0].hojas.append(TerminalGenerico(t.slice[3], getNoNodo()))
        t[0].hojas.append(t[4])
    elif t[1] == "if":
        t.slice[0].type="IF";
        t[0] = InstruccionIf(t.slice[0], getNoNodo())
        t[0].hojas.append(t[2])
        t[0].hojas.append(TerminalGenerico(t.slice[3], getNoNodo()))
        t[0].hojas.append(t[4])
        t[0].hojas.append(TerminalGenerico(t.slice[5], getNoNodo()))
        if t[6] is not None:
            t[0].hojas.append(t[6])
    
    elif t[1] == "while":
        t.slice[0].type="WHILE";
        t[0] = InstruccionWhile(t.slice[0], getNoNodo())
        t[0].hojas.append(t[2])
        t[0].hojas.append(TerminalGenerico(t.slice[3], getNoNodo()))
        t[0].hojas.append(t[4])
        t[0].hojas.append(TerminalGenerico(t.slice[5], getNoNodo()))


def p_opcionfor(t):
    '''opcionfor    : logica
                    | ENTERO PT PT logica
                    | empty '''

def p_unelse(t):
    '''unelse   : ELSE LLAVEIZQ instrucciones LLAVEDER
                | ELSE IF logica LLAVEIZQ instrucciones LLAVEDER unelse
                | empty '''
    if len(t) == 5:
        t.slice[0].type="ELSE"
        t[0] = InstruccionElse(t.slice[0], getNoNodo())
        t[0].hojas.append(TerminalGenerico(t.slice[1], getNoNodo()))
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
        t[0].hojas.append(TerminalGenerico(t.slice[4], getNoNodo()))
    elif len(t) == 8:
        t.slice[0].type="ELSE IF"
        t[0] = InstruccionElseIf(t.slice[0], getNoNodo())
        t[0].hojas.append(t[3])
        t[0].hojas.append(TerminalGenerico(t.slice[4], getNoNodo()))
        t[0].hojas.append(t[5])
        t[0].hojas.append(TerminalGenerico(t.slice[6], getNoNodo()))
        if t[7] is not None:
            t[0].hojas.append(t[7])
    else:
        t[0] = None

def p_logica(t):
    '''logica   : logica AND logica
                | logica OR logica
                | NOT logica
                | rel'''
    if len(t)== 2:
        t[0]=t[1]

def p_rel(t):
    '''rel  : rel IGUAL IGUAL rel
            | rel MENOR rel
            | rel MAYOR rel
            | rel MEIGUAL rel
            | rel MAIGUAL rel
            | rel DIS rel
            | expresion'''
    if len(t)== 2:
        t[0]=t[1]

    elif t[2] == '>': 
        t.slice[0].type="relacional";
        t[0] = NodoMayor(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '<': 
        t.slice[0].type="relacional";
        t[0] = NodoMenor(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '==': 
        t.slice[0].type="relacional";
        t[0] = NodoIgual(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '>=': 
        t.slice[0].type="relacional";
        t[0] = NodoMayorIgual(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '<=': 
        t.slice[0].type="relacional";
        t[0] = NodoMenorIgual(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '!=': 
        t.slice[0].type="relacional";
        t[0] = NodoNigual(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    
            
def p_mutable(t):
    '''mutable  : MUT  
                | empty '''

def p_pyc(t):
    '''pyc  : DPT  
            | empty '''


def p_arrtipos(t):
    '''arrtipos : tipos
                | arreglos
                | empty '''

def p_vectores(t):
    '''vectores : tipos
                | arreglos
                | empty '''

def p_arreglos(t):
    '''arreglos : CORIZQ arreglos PTCOMA ENTERO CORDER
                | tipos
                | ID'''

def p_tipos(t):
    '''tipos    : I64
                | F64
                | BOOL
                | CHAR
                | STRING
                | AMP STR
                | USIZE'''



def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion MOD expresion
                  | expresion AS  tipos'''

    if t[2] == '+'  : 
        t[0] = NodoSuma(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])

    elif t[2] == '-': 
        t[0] = NodoResta(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '*': 
        t[0] = NodoMultiplicacion(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])
    elif t[2] == '/': 
        t[0] = NodoDivision(t.slice[0], getNoNodo())
        t[0].hojas.append(t[1])
        t[0].hojas.append(TerminalGenerico(t.slice[2], getNoNodo()))
        t[0].hojas.append(t[3])

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    #[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ logica PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL
                    | FORM
                    | TRUE
                    | FALSE
                    | VECM NOT listarreglo
                    | ID listarreglo
                    | ID PARIZQ listexpr PARDER
                    | listarreglo'''

    if type(t[1]) is float:
        print("es un decimal")
        t[0] = TerminalDecimal(t.slice[1], getNoNodo())
        
    elif type(t[1]) is int:
        print("es un int")
        t[0] = TerminalEntero(t.slice[1], getNoNodo())
        
    elif type(t[1]) is TerminalCadena:
        print("es un string")
        t[0] =t.slice[1].value

    elif len(t)==3 and t[2]==None:
        print("es un id")
        t[0] = TerminalIdentificador(t.slice[1], getNoNodo())
    
    elif t[1]=="true" or t[1]== "false":
        print("si es")
        t[0] = TerminalBool(t.slice[1], getNoNodo())
    


def p_expresion_mod(t):
    '''expresion    : opcionpow DPT DPT expresion'''

def p_opcionpow(t):
    '''opcionpow    : expresion
                    | tipos'''

def p_expresion_pow(t):
    '''expresion    : POW PARIZQ ENTERO COMA ENTERO PARDER
                    | POWF PARIZQ DECIMAL COMA DECIMAL PARDER'''


def p_expresion_loop(t):
    '''expresion    : LOOP LLAVEIZQ instrucciones LLAVEDER'''


def p_expresion_fnativas(t):
    '''expresion    : expresion PT TOSTRING PARIZQ PARDER
                    | expresion PT SQRT PARIZQ PARDER
                    | expresion PT ABS PARIZQ PARDER
                    | expresion PT CLONE PARIZQ PARDER
                    | expresion PT LEN PARIZQ PARDER
                    | expresion PT TOOWNED PARIZQ PARDER'''


def p_listarreglo(t):
    '''listarreglo  : listarreglo CORIZQ listexpr CORDER
                    | empty '''

def p_listexpr(t):
    '''listexpr : listexpr COMA expresion
                | expresion'''
    

def p_empty(t):
    'empty :'
    pass


def p_error(t):
    print("Error sintáctico en '%s'"  % t.lexer.lineno)

import ply.yacc as yacc
parser = yacc.yacc()

def getNoNodo():
    global noNode
    noNode = noNode + 1
    return noNode