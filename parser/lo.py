tokens  = (
    'LOOP',
    'MOD2',
    'FN',
    'MAIN',
    'FORM',
    'PRINT',
    'TRUE',
    'FALSE',
    'I64',
    'F64',
    'BOOL',
    'CHAR',
    'STRING',
    'STR',
    'USIZE',
    'LET',
    'MUT',
    'STRUCT',
    'VEC',
    'VECM',
    'POW',
    'POWF',
    'MOD',
    'ID',
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
    'COMA',
    'DPT2',
    'DPT',
    'IGUAL2',
    'MEIGUAL',
    'MAIGUAL',
    'MENOR',
    'MAYOR',
    'DIS',
    'IGUAL',
    'AND',
    'OR',
    'NOT',
    'STRING2',
    'CORIZQ2',
    'CORDER2'
)

# Tokens
t_LOOP      = r'loop'
t_MOD2      = r'mod'
t_FN        = r'fn'
t_MAIN     = r'main'
t_FORM      = r'\"([^\"]|{}|{:\?})+\"'
t_PRINT     = r'println!'
t_TRUE      = r'true'
t_FALSE     = r'false'
t_I64       = r'i64'
t_F64       = r'f64'
t_BOOL      = r'bool'
t_CHAR      = r'char'
t_STRING    = r'String'
t_STR       = r'&str'
t_USIZE     = r'usize'
t_LET       = r'let'
t_MUT       = r'mut'     
t_STRUCT    = r'struct'
t_VEC       = r'Vec'
t_VECM      = r'vec!'
t_POW       = r'pow'
t_POWF      = r'powf'
t_MOD       = r'%'
t_ID        = r'([A-Za-z]|_)([A-Za-z]|_|\d)*'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PTCOMA    = r';'
t_COMA      = r','
t_DPT2      = r'::'
t_DPT       = r':'
t_IGUAL2    = r'=='
t_MEIGUAL   = r'<='
t_MAIGUAL   = r'>='
t_MENOR     = r'<'
t_MAYOR     = r'>'
t_DIS       = r'!='
t_IGUAL     = r'='
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'
t_STRING2   = r'\"[^\"{]*\"'
t_CORIZQ2   = r'\{'
t_CORDER2   = r'\}'




def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
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
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

def p_funciones_evaluar(t):
    'funcion  : MOD2'
    print("algo")

def p_funciones_evaluar(t):
    '''funcion  : FN MOD2 PARIZQ expresion PARDER CORDER PTCOMA
                | MAIN PARIZQ PARDER LLAVEIZQ LLAVEDER '''


def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion '''

def p_instrucciones_eval(t):
    '''instruccion  : LET mutable ID pyc tipos IGUAL expresion PTCOMA
                    | PRINT PARIZQ FORM formato PARDER PTCOMA'''
    
def p_formato(t):
    '''formato  : formato COMA impresiones 
                | empty '''

def p_impresiones(t):
    '''impresiones  : ID 
                    | expresion '''

def p_mutable(t):
    '''mutable  : MUT  
                | empty '''

def p_pyc(t):
    '''pyc  : DPT  
            | empty '''

def p_tipos(t):
    '''tipos    : I64
                | F64
                | BOOL
                | CHAR
                | STRING
                | STR
                | USIZE
                | empty '''



def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''


def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL
                    | STRING2'''
    t[0] = t[1]

def p_empty(t):
    'empty :'
    pass
