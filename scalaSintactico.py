import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from scalaLexer import tokens


def p_cuerpo(p):
    """cuerpo : expression
             | sentencia
             | declararVariable
             | declararConstante"""

def p_declararConstante(p):
    """declararConstante : VAL ID COLON tipoValueCons
                        | VAL ID COLON tipo
                        | VAL ID EQUAL valueCons
                        | VAL ID EQUAL expression"""

def p_declararVariable(p):
    """declararVariable : VAR ID COLON tipoValue
                        | VAR ID COLON tipo
                        | VAR ID EQUAL value
                        | VAR ID EQUAL expression"""

def p_value(p):
    """value : string
            | booleano
            | NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN
            | NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN
            | NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN
            | NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN
            | ARRAY LPAREN elementosInternos RPAREN"""

def p_elementosInternos(p):
    """elementosInternos : elementosInternosInt
            | elementosInternosDouble
            | elementosInternosBool
            | elementosInternosString"""

def p_elementosInternosInt(p):
    """elementosInternosInt : int
            | int COMMA elementosInternosInt"""

def p_elementosInternosDouble(p):
    """elementosInternosDouble : double
            | double COMMA elementosInternosDouble"""

def p_elementosInternosBool(p):
    """elementosInternosBool : booleano
            | booleano COMMA elementosInternosBool"""

def p_elementosInternosString(p):
    """elementosInternosString : string
            | string COMMA elementosInternosString"""

def p_valueCons(p):
    """valueCons : string
            | booleano """

def p_tipo(p):
    """tipo : INT
             | DOUBLE
             | BOOL
             | STRING_TYPE"""

def p_tipoValue(p):
    """tipoValue : STRING_TYPE EQUAL string
                | BOOL EQUAL booleano
                | INT EQUAL int
                | DOUBLE EQUAL double
                | ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN
                | ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN
                | ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN
                | ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN"""

def p_tipoValueCons(p):
    """tipoValueCons : STRING_TYPE EQUAL string
                | BOOL EQUAL booleano
                | INT EQUAL int
                | DOUBLE EQUAL double
                | tupla"""

def p_tupla(p):
    'LPAREN  elementos RPAREN'

def p_elementos(p):
    'string COMMA string'


def p_expression_plus(p):
    'expression : expression PLUS term'


def p_expression_minus(p):
    'expression : expression MINUS term'


def p_expression_term(p):
    'expression : term'


def p_term_times(p):
    'term : term TIMES factor'


def p_term_div(p):
    'term : term DIVIDE factor'


def p_term_factor(p):
    'term : factor'


def p_sentencia_if(p):
    'sentencia : IF factor comparacion factor LBRACE cuerpo RBRACE'


def p_comparacion(p):
    '''comparacion : GT
                    | GE
                    | LT
                    | LE
                    | EQUAL2'''

def p_factor_int(p):
    'factor : INT_NUMBER'

def p_factor_double(p):
    'factor : DOUBLE_NUMBER'

def p_booleano(p):
    '''booleano : TRUE
                | FALSE'''

def p_string(p):
    'string : STRING'

def p_double(p):
    'double : DOUBLE_NUMBER'

def p_int(p):
    'int : INT_NUMBER'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
