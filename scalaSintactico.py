import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from scalaLexer import tokens

def p_cuerpo(p):
    """cuerpo : expression
             | sentencia
             | declararVariable
             | declararConstante
             | funcionesTupla
             | funcionesArray
             | for
             | funcionesPropias
             | comparacionesVar"""

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
            | ARRAY LPAREN elementosInternos RPAREN
            | LIST LPAREN elementosInternos RPAREN"""

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

def p_elementosInternos2(p):
    """elementosInternos2 : int
            | double
            | booleano
            | string
            | int COMMA elementosInternos2
            | double COMMA elementosInternos2
            | booleano COMMA elementosInternos2
            | string COMMA elementosInternos2"""

def p_valueCons(p):
    """valueCons : string
            | booleano
            | tupla"""

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
                | ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN
                | LIST LBRACK INT RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK DOUBLE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK BOOL RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK STRING_TYPE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN"""

def p_tipoValueCons(p):
    """tipoValueCons : STRING_TYPE EQUAL string
                | BOOL EQUAL booleano
                | INT EQUAL int
                | DOUBLE EQUAL double"""

def p_tupla(p):
    'tupla : LPAREN elementosInternos2 RPAREN'

def p_funcionesTupla(p):
    """funcionesTupla : tuplaSwap
                | tuplaToString
                | tuplaProductIterator"""

def p_tuplaSwap(p):
    'tuplaSwap : ID DOT SWAP'

def p_tuplaToString(p):
    'tuplaToString : ID DOT TOSTRING LPAREN RPAREN'

def p_tuplaProductIterator(p):
    'tuplaProductIterator : ID DOT PRODUCTITERATOR'

def p_funcionesArray(p):
    """funcionesArray : arrayHead
            | arrayTail
            | arrayLength"""

def p_funcionesPropias(p):
    """funcionesPropias : INPUT LPAREN RPAREN
            | PRINTLN LPAREN string RPAREN
            | PRINTLN LPAREN booleano RPAREN
            | PRINTLN LPAREN ID RPAREN
            | PRINTLN LPAREN expression RPAREN"""

def p_arrayHead(p):
    """arrayHead : ID DOT HEAD"""

def p_arrayTail(p):
    """arrayTail : ID DOT TAIL"""

def p_arrayLength(p):
    """arrayLength : ID DOT LENGTH"""

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


def p_for(p):
    'for : FOR LPAREN ID LM ID RPAREN LBRACE  cuerpo  RBRACE'


def p_comparacionesVar(p):
    '''comparacionesVar : ID DOT EQUALS LPAREN ID  RPAREN
                        | ID DOT EQ LPAREN ID RPAREN'''

def p_comparacion(p):
    '''comparacion : GT
                    | GE
                    | LT
                    | LE
                    | EQUAL2'''

def p_factor_int(p):
    'factor : int'

def p_factor_double(p):
    'factor : double'

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