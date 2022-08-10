
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
    'as'  : 'AS',

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
     r'\"([^\"]|{}|{:\?})*\"'
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

import Analyzer.ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática

def p_funciones_lista(t):
    '''funciones    : funciones funcion 
                    | funcion '''

def p_funciones_evaluar(t):
    '''funcion  : PUB FN ID PARIZQ parametros PARDER tipofun LLAVEIZQ instrucciones LLAVEDER
                | FN ID PARIZQ parametros PARDER tipofun LLAVEIZQ instrucciones LLAVEDER
                | PUB MODF ID LLAVEIZQ funciones LLAVEDER
                | MODF ID LLAVEIZQ funciones LLAVEDER
                | FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER
                | STRUCT ID LLAVEIZQ liststruct LLAVEDER'''

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
    '''instrucciones    : instrucciones instruccion 
                        | instruccion '''

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

def p_opcionfor(t):
    '''opcionfor    : logica
                    | ENTERO PT PT logica
                    | empty '''

def p_unelse(t):
    '''unelse   : ELSE LLAVEIZQ instrucciones LLAVEDER
                | ELSE IF logica LLAVEIZQ instrucciones LLAVEDER unelse
                | empty '''

def p_logica(t):
    '''logica   : logica AND logica
                | logica OR logica
                | NOT logica
                | rel'''


def p_rel(t):
    '''rel  : rel IGUAL IGUAL rel
            | rel MENOR rel
            | rel MAYOR rel
            | rel MEIGUAL rel
            | rel MAIGUAL rel
            | rel DIS rel
            | expresion'''

            
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
                  | expresion AS tipos'''


def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

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
    t[0] = t[1]


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

import Analyzer.ply.yacc as yacc
parser = yacc.yacc()
