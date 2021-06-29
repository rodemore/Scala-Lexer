import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for' : 'FOR',
    'while': 'WHILE',
    'this' : 'THIS',
    'new' : 'NEW',
    'return' : 'RETURN',
    'object' : 'OBJECT',
    'def' : 'DEF',
    'Unit' : 'unit',
    'class' : 'CLASS',
    'var' : 'VAR',
    'val' : 'VAL'
}

tokens = (
    'INT',  #int
    'DOUBLE',  #double
    'BOOL',  #bool
    'STRING_TYPE',  #string
    'ARRAY',  #array
    'LIST',  #list
    'ID',  #var/function name
    'EQUAL2',  # ==
    'EQUAL',  # =
    'INT_NUMBER',  #1234
    'DOUBLE_NUMBER',  #7.999
    'STRING',  # "example string"
    'TRUE',  # true
    'FALSE',  # false
    'LBRACE',  # {
    'RBRACE',  # } nota: agregar pto y coma???
    'PLUS',  # +
    'MINUS',  # -
    'TIMES',  # *
    'DIVIDE',  # /
    'MOD',  # %
    'LPAREN',  # (
    'RPAREN',  # )
    'INCREMENT',  # ++
    'DECREMENT',  # --
    'LBRACK',  # [
    'RBRACK',  # ]
    'GT',  # >
    'GE',  # >=
    'LT',  # <
    'LE',  # <=
    'COMMA',  # ,
    'COLON',  # :
    'SEMICOLON',  # ;
    'PRINTLN',
    'EQUALS',
    'DOT',
    'EQ',
    'SWAP',
    'TOSTRING',
    'PRODUCTITERATOR',
    'HEAD',
    'TAIL',
    'ISEMPTY',
    'REVERSE',
    'LENGTH',
    'INPUT'

) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_EQUAL2 = r'=='
t_EQUAL = r'='
t_LBRACE = r'{'
t_RBRACE = r'}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_DOT = r'\.'

def t_INT(t):
    r'Int'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_BOOL(t):
    r'boolean'
    return t

def t_ARRAY(t):
    r'Array'
    return t

def t_LIST(t):
    r'List'
    return t

def t_STRING_TYPE(t):
    r'String'
    return t

def t_EQUALS(t):
    r'equals'
    return t

def t_EQ(t):
    r'eq'
    return t

def t_SWAP(t):
    r'swap'
    return t

def t_HEAD(t):
    r'head'
    return t

def t_TAIL(t):
    r'tail'
    return t

def t_ISEMPTY(t):
    r'isEmpty'
    return t

def t_REVERSE(t):
    r'reverse'
    return t

def t_LENGTH(t):
    r'length'
    return t

def t_TOSTRING(t):
    r'toString'
    return t

def t_PRODUCTITERATOR(t):
    r'productIterator'
    return t

def t_PRINTLN(t):
    r'System.out.println'
    return t

def t_INPUT(t):
    r'scala.io.StdIn.readLine'
    return t

def t_DOUBLE_NUMBER(t):
    r'[0-9]+(?:\.[0-9]*)'
    t.value = float(t.value)
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# A regular expression rule with some action code
def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

# Build the lexer
lexer = lex.lex()

#linea=" "
#while linea!="":
#    linea=input(">>")
#    lexer.input(linea)
#    getTokens(lexer)
#    print()

# Tokenize
#print("Succesfull")
