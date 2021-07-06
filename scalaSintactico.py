import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from scalaLexer import tokens


def p_cuerpoP(p):
    '''cuerpoP : cuerpo
             | defFunciones'''

def p_cuerpo(p):
    """cuerpo : expression
             | sentencia
             | declararVariable
             | declararConstante
             | funcionesTupla
             | funcionesList
             | funcionesArray
             | for
             | funcionesPropias
             | while
             | funciones
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
            | valueArray"""

def p_valueArray(p):
    'valueArray : ARRAY LPAREN elementosInternos RPAREN'


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
            | tupla
            | valueList"""

def p_valueList(p):
    'valueList : LIST LPAREN elementosInternos RPAREN'

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
                | LIST LBRACK INT RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK DOUBLE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK BOOL RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK STRING_TYPE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN"""

def p_tupla(p):
    'tupla : LPAREN elementosInternos2 RPAREN'

def p_funcionesTupla(p):
    """funcionesTupla : tuplaSwap
                | tuplaToString
                | tuplaProductIterator"""

def p_tuplaSwap(p):
    'tuplaSwap : tupla DOT SWAP'

def p_tuplaToString(p):
    'tuplaToString : tupla DOT TOSTRING LPAREN RPAREN'

def p_tuplaProductIterator(p):
    'tuplaProductIterator : tupla DOT PRODUCTITERATOR'


def p_funcionesArray(p):
    """funcionesArray : arrayHead
            | arrayTail
            | arrayLength"""


def p_funcionesList(p):
    """funcionesList : listIsEmpty
            | listReverse
            | listHead"""


def p_funcionesPropias(p):
    """funcionesPropias : INPUT LPAREN RPAREN
            | PRINTLN LPAREN string RPAREN
            | PRINTLN LPAREN booleano RPAREN
            | PRINTLN LPAREN ID RPAREN
            | PRINTLN LPAREN expression RPAREN"""



def p_arrayHead(p):
    """arrayHead : valueArray DOT HEAD"""

def p_arrayTail(p):
    """arrayTail : valueArray DOT TAIL"""

def p_arrayLength(p):
    """arrayLength : valueArray DOT LENGTH"""

def p_listReverse(p):
    'listReverse : valueList DOT REVERSE'

def p_listIsEmpty(p):
    'listIsEmpty : valueList DOT ISEMPTY'

def p_listHead(p):
    'listHead : valueList DOT HEAD'

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
    'if : IF LPAREN compclause RPAREN LBRACE cuerpo RBRACE'


def p_sentencia_else(p):
    '''sentencia : if
                 | if ELSE LBRACE cuerpo RBRACE'''


def p_comp(p):
    "comp : factor comparacion factor"

def p_while(p):
    'while : WHILE LPAREN compclause RPAREN LBRACE cuerpo RBRACE'

def p_compclause(p):
    """compclause : comp
                | booleano"""


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


def p_defFunciones(p):
    """defFunciones : DEF ID LPAREN parametros RPAREN COLON UNIT EQUAL LBRACE cuerpo RBRACE
                    | DEF ID LPAREN RPAREN COLON UNIT EQUAL LBRACE cuerpo RBRACE
                    | DEF ID LPAREN parametros RPAREN COLON tipo EQUAL LBRACE cuerpo RETURN ID RBRACE
                    | DEF ID LPAREN RPAREN COLON tipo EQUAL LBRACE cuerpo RETURN ID RBRACE"""

def p_funciones(p):
    '''funciones : ID LPAREN RPAREN
                    | ID LPAREN argumentos RPAREN'''

def p_parametros(p):
    """parametros : ID COLON tipo
                    | ID COLON tipo COMMA parametros"""

def p_argumentos(p):
    '''argumentos : int
                    | double
                    | booleano
                    | string
                    | int COMMA argumentos
                    | double COMMA argumentos
                    | booleano COMMA argumentos
                    | string COMMA argumentos'''


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
