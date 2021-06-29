import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from scalaLexer import tokens



def p_cuerpo(p):
    """cuerpo : expression
             | sentencia 
             | declararVariable"""

def p_declararVariable(p):
    """declararVariable : VAR ID COLON tipoValue
                        | VAR ID COLON tipo
                        | VAR ID EQUAL value
                        | VAR ID EQUAL expression
                        | VAR ID EQUAL expression
                        | VAR ID COLON LPAREN ARRAY RPAREN expressionarray """

def p_value(p):
    """value : string
            | booleano """

def p_tipo(p):
    """tipo : INT
             | DOUBLE
             | BOOL
             | STRING_TYPE"""

def p_newarray(p):
    """value : NEW ARRAY LBRACK tipo RBRACK LPAREN int RPAREN
        """

def p_newarray(p):
    """value : NEW ARRAY LBRACK tipo RBRACK LPAREN int RPAREN
        """

def p_tipoValue(p):
    """tipoValue : STRING_TYPE EQUAL string
                | BOOL EQUAL booleano
                | INT EQUAL int
                | DOUBLE EQUAL double"""


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
                    | LE'''

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