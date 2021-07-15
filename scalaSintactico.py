import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from scalaLexer import tokens


def p_cuerpoP(p):
    '''cuerpoP : cuerpo
             | defFunciones'''
    p[0] = p[1]

def p_cuerpo(p):
    """cuerpo : expression
             | sentencia
             | declararVariable
             | declararConstante
             | asignarVariable
             | asignarConstante
             | funcionesTupla
             | funcionesList
             | funcionesArray
             | for
             | funcionesPropias
             | while
             | funciones
             | comparacionesVar
             | asignar
             | cuerpo sep cuerpo
             | printVacio
             | dobleSuma
             | headInt
             | whileSinCerrar"""
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_sep(p):
    """sep : SEMICOLON """

def p_asignar(p):
    """asignar :  ID EQUAL expression"""
    p[0] = ('asignacion', p[1], p[2], p[3])

def p_asignarConstante(p):
    """asignarConstante : VAL ID COLON tipoValueCons
                        | VAL ID EQUAL valueCons
                        | VAL ID EQUAL expression"""
    p[0] = ('asignacion', p[1], p[2], p[3], p[4])

def p_declararConstante(p):
    'declararConstante : VAL ID COLON tipo'
    p[0] = ('declaracion', p[1], p[2], p[3], p[4])

def p_asignarVariable(p):
    """asignarVariable : VAR ID COLON tipoValue
                        | VAR ID EQUAL value
                        | VAR ID EQUAL expression"""
    p[0] = ('asignacion', p[1], p[2], p[3], p[4])

def p_declararVariable(p):
    'declararVariable : VAR ID COLON tipo'
    p[0] = ('declaracion', p[1], p[2], p[3], p[4])

def p_value(p):
    """value : valueSingle
            | valueNewAr
            | valueArray"""
    p[0] = p[1]

def p_valueSingle(p):
    """valueSingle : string
                    | booleano"""
    p[0] = p[1]

def p_valueNewAr(p):
    """valueNewAr :  NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN
                | NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN
                | NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN
                | NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN"""
    p[0] = ('array', p[1]+ p[2]+p[3]+p[4]+p[5]+p[6]+str(p[7])+p[8])

def p_valueArray(p):
    'valueArray : ARRAY LPAREN elementosInternos RPAREN'
    p[0] = ('array', p[1]+ p[2]+p[3]+p[4])

def p_elementosInternos(p):
    """elementosInternos : elementosInternosInt
            | elementosInternosDouble
            | elementosInternosBool
            | elementosInternosString"""
    p[0] = p[1]

def p_elementosInternosInt(p):
    """elementosInternosInt : int
            | int COMMA elementosInternosInt"""
    if len(p)==2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) +p[2]+ str(p[3])

def p_elementosInternosDouble(p):
    """elementosInternosDouble : double
            | double COMMA elementosInternosDouble"""
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) + p[2]+ str(p[3])

def p_elementosInternosBool(p):
    """elementosInternosBool : booleano
            | booleano COMMA elementosInternosBool"""
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) + p[2]+ str(p[3])

def p_elementosInternosString(p):
    """elementosInternosString : string
            | string COMMA elementosInternosString"""
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2] + p[3]

def p_elementosInternos2(p):
    """elementosInternos2 : int
            | double
            | booleano
            | string
            | int COMMA elementosInternos2
            | double COMMA elementosInternos2
            | booleano COMMA elementosInternos2
            | string COMMA elementosInternos2"""
    if len(p)==2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) + p[2]+ p[3]

def p_valueCons(p):
    """valueCons : string
            | booleano
            | tupla
            | valueList"""

    p[0] = str(p[1])

def p_valueList(p):
    'valueList : LIST LPAREN elementosInternos RPAREN'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_tipo(p):
    """tipo : INT
             | DOUBLE
             | BOOL
             | STRING_TYPE"""
    p[0] = p[1]


def p_tipoValue(p):
    """tipoValue : STRING_TYPE EQUAL string
                | BOOL EQUAL booleano
                | INT EQUAL int
                | DOUBLE EQUAL double
                | ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN
                | ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN
                | ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN
                | ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN"""
    if len(p) == 4:
        p[0] = ('dato', p[1] + p[2] + str(p[3]))
    else:
        p[0] = ('array', p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9] + p[10] + p[11] + str(p[12]) + p[13])

def p_tipoValueCons(p):
    """tipoValueCons : STRING_TYPE EQUAL string
                | BOOL EQUAL booleano
                | INT EQUAL int
                | DOUBLE EQUAL double
                | LIST LBRACK INT RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK DOUBLE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK BOOL RBRACK EQUAL LIST LPAREN elementosInternos RPAREN
                | LIST LBRACK STRING_TYPE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN"""
    if len(p) == 4:
        p[0] = ('dato', p[1] + p[2] + str(p[3]))
    else:
        p[0] = ('lista', p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9])

def p_tupla(p):
    'tupla : LPAREN elementosInternos2 RPAREN'
    p[0] = ('tupla', p[1] + p[2] + p[3])

def p_funcionesTupla(p):
    """funcionesTupla : tuplaSwap
                | tuplaToString
                | tuplaProductIterator"""
    p[0] = p[1]

def p_tuplaSwap(p):
    'tuplaSwap : tupla DOT SWAP'
    p[0] = ('funcionTupla', p[1], p[3])

def p_tuplaToString(p):
    'tuplaToString : tupla DOT TOSTRING LPAREN RPAREN'
    p[0] = ('funcionTupla', p[1], p[3]+p[4]+p[5])

def p_tuplaProductIterator(p):
    'tuplaProductIterator : tupla DOT PRODUCTITERATOR'
    p[0] = ('funcionTupla', p[1], p[3])


def p_funcionesArray(p):
    """funcionesArray : arrayHead
            | arrayTail
            | arrayLength"""
    p[0] = p[1]


def p_funcionesList(p):
    """funcionesList : listIsEmpty
            | listReverse
            | listHead"""
    p[0] = p[1]

def p_funcionesPropias(p):
    """funcionesPropias : INPUT LPAREN RPAREN
            | PRINTLN LPAREN string RPAREN
            | PRINTLN LPAREN booleano RPAREN
            | PRINTLN LPAREN ID RPAREN
            | PRINTLN LPAREN RPAREN
            | PRINTLN LPAREN expression RPAREN"""
    if len(p)==4:
        p[0] = ('funcionPropia', p[1]+p[2]+p[3])
    else:
        p[0] = ('funcionPropia', p[1]+p[2]+p[4], p[3])

def p_printVacio(p):
    'printVacio : PRINTLN LPAREN RPAREN'
    print('Error: println function cannot have empty argument at line:', p.lexer.lineno)

def p_dobleSuma(p):
    'dobleSuma : factor PLUS PLUS factor'
    print('Error: operator \'++\' cannot go followed by operand at line', p.lexer.lineno)

def p_headInt(p):
    'headInt : factor DOT HEAD'
    print('Error: Invalid use of HEAD at line', p.lexer.lineno)

def p_whileSinCerrar(p):
    'whileSinCerrar : WHILE LPAREN compclause RPAREN LBRACE cuerpo'
    print('Error: Missing closing Brace \'}\'')

def p_arrayHead(p):
    """arrayHead : valueArray DOT HEAD"""
    p[0] = ('funcionArray', p[1], p[3])

def p_arrayTail(p):
    """arrayTail : valueArray DOT TAIL"""
    p[0] = ('funcionArray', p[1], p[3])

def p_arrayLength(p):
    """arrayLength : valueArray DOT LENGTH"""
    p[0] = ('funcionArray', p[1], p[3])

def p_listReverse(p):
    'listReverse : valueList DOT REVERSE'
    p[0] = ('funcionLista', p[1], p[3])

def p_listIsEmpty(p):
    'listIsEmpty : valueList DOT ISEMPTY'
    p[0] = ('funcionLista', p[1], p[3])

def p_listHead(p):
    'listHead : valueList DOT HEAD'
    p[0] = ('funcionLista', p[1], p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_sentencia_if(p):
    'if : IF LPAREN compclause RPAREN LBRACE cuerpo RBRACE'
    p[0] = ('sentenciaif', p[1], p[3], p[6])


def p_sentencia_else(p):
    '''sentencia : if
                 | if ELSE LBRACE cuerpo RBRACE'''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = ('sentencia', p[1], p[2], p[4])


def p_comp(p):
    "comp : factor comparacion factor"
    p[0] = ('comparacion', p[1], p[2], p[3])


def p_while(p):
    'while : WHILE LPAREN compclause RPAREN LBRACE cuerpo RBRACE'
    p[0] = ('while', p[3], p[6])

def p_compclause(p):
    """compclause : comp
                | booleano"""
    p[0] = p[1]

def p_for(p):
    'for : FOR LPAREN ID LM ID RPAREN LBRACE  cuerpo  RBRACE'
    p[0] = ('for', p[1], p[3], p[4], p[5],p[8])


def p_comparacionesVar(p):
    '''comparacionesVar : ID DOT EQUALS LPAREN ID  RPAREN
                        | ID DOT EQ LPAREN ID RPAREN'''
    p[0] = ('comparaciones', p[1], p[3], p[5])


def p_comparacion(p):
    '''comparacion : GT
                    | GE
                    | LT
                    | LE
                    | EQUAL2'''
    p[0] = p[1]

def p_defFunciones(p):
    """defFunciones : DEF ID LPAREN parametros RPAREN COLON UNIT EQUAL LBRACE cuerpo RBRACE
                    | DEF ID LPAREN RPAREN COLON UNIT EQUAL LBRACE cuerpo RBRACE
                    | DEF ID LPAREN parametros RPAREN COLON tipo EQUAL LBRACE cuerpo RETURN ID RBRACE
                    | DEF ID LPAREN RPAREN COLON tipo EQUAL LBRACE cuerpo RETURN ID RBRACE"""
    if len(p)==12:
        p[0] = ('definicFuncion', p[1], p[2],p[4], p[6], p[7], p[8], p[10])
    elif len(p)==11:
        p[0] = ('definicFuncion', p[1], p[2],p[5], p[6], p[7], p[9])
    elif len(p)==14:
        p[0] = ('definicFuncion', p[1], p[2],p[4], p[6], p[7], p[8], p[10], p[11], p[12])
    else:
        p[0] = ('definicFuncion', p[1], p[2],p[5], p[6], p[7], p[9], p[10], p[11])

def p_funciones(p):
    '''funciones : ID LPAREN RPAREN
                    | ID LPAREN argumentos RPAREN'''
    if len(p)==4:
        p[0] = ('Funcion', p[1] + p[2] + p[3])
    else:
        p[0] = ('Funcion', p[1] + p[2] + p[4], p[3])

def p_parametros(p):
    """parametros : ID COLON tipo
                    | ID COLON tipo COMMA parametros"""
    if len(p)==4:
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = p[1] + p[2] + p[3] + p[5]

def p_argumentos(p):
    '''argumentos : int
                    | double
                    | booleano
                    | string
                    | int COMMA argumentos
                    | double COMMA argumentos
                    | booleano COMMA argumentos
                    | string COMMA argumentos'''
    if len(p)==2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) +p[2]+ p[3]

def p_factor_int(p):
    'factor : int'
    p[0] = ('INT', str(p[1]))

def p_factor_double(p):
    'factor : double'
    p[0] = ('DOUBLE',str(p[1]))

def p_booleano(p):
    '''booleano : TRUE
                | FALSE'''
    p[0] = str(p[1])

def p_string(p):
    'string : STRING'
    p[0] = p[1]

def p_double(p):
    'double : DOUBLE_NUMBER'
    p[0] = str(p[1])

def p_int(p):
    'int : INT_NUMBER'
    p[0] = str(p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! Error can found at line:", p.lexer.lineno)
    error_status[0] = [True]


# Build the parser
parser = yacc.yacc()
error_status = [False]



while True:
  try:
      s = input('calc > ')
  except EOFError:
      break
  if not s: continue
  result = parser.parse(s)
  print(result)

