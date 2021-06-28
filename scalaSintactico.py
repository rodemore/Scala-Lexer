import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from scalaLexer import tokens

def p_cuerpo(p):
    """cuerpo : expression
             | sentencia """

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


def p_booleano_expr(p):
    '''booleano : TRUE
                | FALSE'''


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