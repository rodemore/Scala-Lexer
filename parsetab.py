
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

<<<<<<< HEAD
_lr_signature = 'ARRAY BOOL CLASS COLON COMMA DECREMENT DEF DIVIDE DOT DOUBLE DOUBLE_NUMBER ELSE EQ EQUAL EQUAL2 EQUALS FALSE FOR GE GT HEAD ID IF INCREMENT INT INT_NUMBER ISEMPTY LBRACE LBRACK LE LENGTH LIST LPAREN LT MINUS MOD NEW OBJECT PLUS PRINTLN PRODUCTITERATOR RBRACE RBRACK RETURN REVERSE RPAREN SEMICOLON STRING STRING_TYPE SWAP TAIL THIS TIMES TOSTRING TRUE VAL VAR WHILE unitcuerpo : expression\n             | sentencia\n             | declararVariabledeclararVariable : VAR ID COLON tipoValue\n                        | VAR ID COLON tipo\n                        | VAR ID EQUAL value\n                        | VAR ID EQUAL expressionvalue : string\n            | booleano tipo : INT\n             | DOUBLE\n             | BOOL\n             | STRING_TYPEtipoValue : STRING_TYPE EQUAL string\n                | BOOL EQUAL booleano\n                | INT EQUAL int\n                | DOUBLE EQUAL doubleexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorsentencia : IF factor comparacion factor LBRACE cuerpo RBRACEcomparacion : GT\n                    | GE\n                    | LT\n                    | LE\n                    | EQUAL2factor : INT_NUMBERfactor : DOUBLE_NUMBERbooleano : TRUE\n                | FALSEstring : STRINGdouble : DOUBLE_NUMBERint : INT_NUMBER'
    
_lr_action_items = {'IF':([0,43,],[6,6,]),'VAR':([0,43,],[8,8,]),'INT_NUMBER':([0,6,11,12,13,14,21,22,23,24,25,26,28,43,46,],[9,9,9,9,9,9,9,-25,-26,-27,-28,-29,9,9,52,]),'DOUBLE_NUMBER':([0,6,11,12,13,14,21,22,23,24,25,26,28,43,47,],[10,10,10,10,10,10,10,-25,-26,-27,-28,-29,10,10,54,]),'$end':([1,2,3,4,5,7,9,10,17,18,19,20,30,31,32,33,34,35,36,37,38,39,40,41,42,49,50,51,52,53,54,55,],[0,-1,-2,-3,-20,-23,-30,-31,-18,-19,-21,-22,-4,-5,-13,-12,-10,-11,-6,-7,-8,-9,-34,-32,-33,-14,-15,-16,-36,-17,-35,-24,]),'RBRACE':([2,3,4,5,7,9,10,17,18,19,20,30,31,32,33,34,35,36,37,38,39,40,41,42,48,49,50,51,52,53,54,55,],[-1,-2,-3,-20,-23,-30,-31,-18,-19,-21,-22,-4,-5,-13,-12,-10,-11,-6,-7,-8,-9,-34,-32,-33,55,-14,-15,-16,-36,-17,-35,-24,]),'PLUS':([2,5,7,9,10,17,18,19,20,37,],[11,-20,-23,-30,-31,-18,-19,-21,-22,11,]),'MINUS':([2,5,7,9,10,17,18,19,20,37,],[12,-20,-23,-30,-31,-18,-19,-21,-22,12,]),'TIMES':([5,7,9,10,17,18,19,20,],[13,-23,-30,-31,13,13,-21,-22,]),'DIVIDE':([5,7,9,10,17,18,19,20,],[14,-23,-30,-31,14,14,-21,-22,]),'ID':([8,],[16,]),'GT':([9,10,15,],[-30,-31,22,]),'GE':([9,10,15,],[-30,-31,23,]),'LT':([9,10,15,],[-30,-31,24,]),'LE':([9,10,15,],[-30,-31,25,]),'EQUAL2':([9,10,15,],[-30,-31,26,]),'LBRACE':([9,10,29,],[-30,-31,43,]),'COLON':([16,],[27,]),'EQUAL':([16,32,33,34,35,],[28,44,45,46,47,]),'STRING_TYPE':([27,],[32,]),'BOOL':([27,],[33,]),'INT':([27,],[34,]),'DOUBLE':([27,],[35,]),'STRING':([28,44,],[40,40,]),'TRUE':([28,45,],[41,41,]),'FALSE':([28,45,],[42,42,]),}
=======
_lr_signature = 'ARRAY BOOL CLASS COLON COMMA DECREMENT DEF DIVIDE DOT DOUBLE DOUBLE_NUMBER ELSE EQ EQUAL EQUALS FALSE FOR GE GT HEAD ID IF INCREMENT INT INT_NUMBER ISEMPTY LBRACE LBRACK LE LENGTH LIST LPAREN LT MINUS MOD NEW OBJECT PLUS PRINTLN PRODUCTITERATOR RBRACE RBRACK RETURN REVERSE RPAREN SEMICOLON STRING STRING_TYPE SWAP TAIL THIS TIMES TOSTRING TRUE VAL VAR WHILE unitdeclararVariable : VAR ID COLON tipoValue\n                        | VAR ID COLON tipo\n                        | VAR ID EQUAL value\n                        | VAR ID EQUAL expressionvalue : string\n            | booleano\n            | NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN\n            | ARRAY LPAREN elementosInternos RPARENelementosInternos : elementosInternosInt\n            | elementosInternosDouble\n            | elementosInternosBool\n            | elementosInternosStringelementosInternosInt : int\n            | int COMMA elementosInternosIntelementosInternosDouble : double\n            | double COMMA elementosInternosDoubleelementosInternosBool : booleano\n            | booleano COMMA elementosInternosBoolelementosInternosString : string\n            | string COMMA elementosInternosStringtipo : INT\n             | DOUBLE\n             | BOOL\n             | STRING_TYPEtipoValue : STRING_TYPE EQUAL string\n                | BOOL EQUAL booleano\n                | INT EQUAL int\n                | DOUBLE EQUAL double\n                | ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPARENcuerpo : expression\n             | sentencia expression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorsentencia : IF factor comparacion factor LBRACE cuerpo RBRACEcomparacion : GT\n                    | GE\n                    | LT\n                    | LEfactor : INT_NUMBERfactor : DOUBLE_NUMBERbooleano : TRUE\n                | FALSEstring : STRINGdouble : DOUBLE_NUMBERint : INT_NUMBER'
    
_lr_action_items = {'VAR':([0,],[2,]),'$end':([1,6,7,8,9,10,11,13,14,15,16,19,20,21,22,23,24,25,37,38,39,40,41,42,47,48,59,60,69,106,107,108,109,126,127,128,129,],[0,-1,-2,-27,-26,-24,-25,-3,-4,-5,-6,-40,-53,-51,-52,-43,-49,-50,-28,-29,-30,-55,-31,-54,-38,-39,-41,-42,-11,-7,-8,-9,-10,-32,-33,-34,-35,]),'ID':([2,],[3,]),'COLON':([3,],[4,]),'EQUAL':([3,8,9,10,11,61,62,63,64,],[5,26,27,28,29,74,75,76,77,]),'STRING_TYPE':([4,30,49,105,],[8,46,68,113,]),'BOOL':([4,30,49,104,],[9,45,67,112,]),'INT':([4,30,49,102,],[10,43,65,110,]),'DOUBLE':([4,30,49,103,],[11,44,66,111,]),'ARRAY':([4,5,17,86,87,88,89,],[12,18,33,94,95,96,97,]),'NEW':([5,74,75,76,77,],[17,86,87,88,89,]),'STRING':([5,26,34,73,],[20,20,20,20,]),'TRUE':([5,27,34,72,],[21,21,21,21,]),'FALSE':([5,27,34,72,],[22,22,22,22,]),'INT_NUMBER':([5,28,31,32,34,35,36,70,90,91,92,93,118,119,120,121,],[24,40,24,24,40,24,24,40,40,40,40,40,40,40,40,40,]),'DOUBLE_NUMBER':([5,29,31,32,34,35,36,71,],[25,42,25,25,42,25,25,42,]),'LBRACK':([12,33,94,95,96,97,],[30,49,102,103,104,105,]),'PLUS':([14,19,23,24,25,47,48,59,60,],[31,-40,-43,-49,-50,-38,-39,-41,-42,]),'MINUS':([14,19,23,24,25,47,48,59,60,],[32,-40,-43,-49,-50,-38,-39,-41,-42,]),'LPAREN':([18,78,79,80,81,114,115,116,117,],[34,90,91,92,93,118,119,120,121,]),'TIMES':([19,23,24,25,47,48,59,60,],[35,-43,-49,-50,35,35,-41,-42,]),'DIVIDE':([19,23,24,25,47,48,59,60,],[36,-43,-49,-50,36,36,-41,-42,]),'COMMA':([20,21,22,40,42,55,56,57,58,],[-53,-51,-52,-55,-54,70,71,72,73,]),'RPAREN':([20,21,22,40,42,50,51,52,53,54,55,56,57,58,82,83,84,85,98,99,100,101,122,123,124,125,],[-53,-51,-52,-55,-54,69,-12,-13,-14,-15,-16,-18,-20,-22,-17,-19,-21,-23,106,107,108,109,126,127,128,129,]),'RBRACK':([43,44,45,46,65,66,67,68,110,111,112,113,],[61,62,63,64,78,79,80,81,114,115,116,117,]),}
>>>>>>> 2fcbf43bc68c3329114fcf4778e5f075909bc071

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

<<<<<<< HEAD
_lr_goto_items = {'cuerpo':([0,43,],[1,48,]),'expression':([0,28,43,],[2,37,2,]),'sentencia':([0,43,],[3,3,]),'declararVariable':([0,43,],[4,4,]),'term':([0,11,12,28,43,],[5,17,18,5,5,]),'factor':([0,6,11,12,13,14,21,28,43,],[7,15,7,7,19,20,29,7,7,]),'comparacion':([15,],[21,]),'tipoValue':([27,],[30,]),'tipo':([27,],[31,]),'value':([28,],[36,]),'string':([28,44,],[38,49,]),'booleano':([28,45,],[39,50,]),'int':([46,],[51,]),'double':([47,],[53,]),}
=======
_lr_goto_items = {'declararVariable':([0,],[1,]),'tipoValue':([4,],[6,]),'tipo':([4,],[7,]),'value':([5,],[13,]),'expression':([5,],[14,]),'string':([5,26,34,73,],[15,37,58,58,]),'booleano':([5,27,34,72,],[16,38,57,57,]),'term':([5,31,32,],[19,47,48,]),'factor':([5,31,32,35,36,],[23,23,23,59,60,]),'int':([28,34,70,90,91,92,93,118,119,120,121,],[39,55,55,98,99,100,101,122,123,124,125,]),'double':([29,34,71,],[41,56,56,]),'elementosInternos':([34,],[50,]),'elementosInternosInt':([34,70,],[51,82,]),'elementosInternosDouble':([34,71,],[52,83,]),'elementosInternosBool':([34,72,],[53,84,]),'elementosInternosString':([34,73,],[54,85,]),}
>>>>>>> 2fcbf43bc68c3329114fcf4778e5f075909bc071

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
<<<<<<< HEAD
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','scalaSintactico.py',9),
  ('cuerpo -> sentencia','cuerpo',1,'p_cuerpo','scalaSintactico.py',10),
  ('cuerpo -> declararVariable','cuerpo',1,'p_cuerpo','scalaSintactico.py',11),
  ('declararVariable -> VAR ID COLON tipoValue','declararVariable',4,'p_declararVariable','scalaSintactico.py',14),
  ('declararVariable -> VAR ID COLON tipo','declararVariable',4,'p_declararVariable','scalaSintactico.py',15),
  ('declararVariable -> VAR ID EQUAL value','declararVariable',4,'p_declararVariable','scalaSintactico.py',16),
  ('declararVariable -> VAR ID EQUAL expression','declararVariable',4,'p_declararVariable','scalaSintactico.py',17),
  ('value -> string','value',1,'p_value','scalaSintactico.py',20),
  ('value -> booleano','value',1,'p_value','scalaSintactico.py',21),
  ('tipo -> INT','tipo',1,'p_tipo','scalaSintactico.py',24),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','scalaSintactico.py',25),
  ('tipo -> BOOL','tipo',1,'p_tipo','scalaSintactico.py',26),
  ('tipo -> STRING_TYPE','tipo',1,'p_tipo','scalaSintactico.py',27),
  ('tipoValue -> STRING_TYPE EQUAL string','tipoValue',3,'p_tipoValue','scalaSintactico.py',30),
  ('tipoValue -> BOOL EQUAL booleano','tipoValue',3,'p_tipoValue','scalaSintactico.py',31),
  ('tipoValue -> INT EQUAL int','tipoValue',3,'p_tipoValue','scalaSintactico.py',32),
  ('tipoValue -> DOUBLE EQUAL double','tipoValue',3,'p_tipoValue','scalaSintactico.py',33),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','scalaSintactico.py',36),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','scalaSintactico.py',40),
  ('expression -> term','expression',1,'p_expression_term','scalaSintactico.py',44),
  ('term -> term TIMES factor','term',3,'p_term_times','scalaSintactico.py',48),
  ('term -> term DIVIDE factor','term',3,'p_term_div','scalaSintactico.py',52),
  ('term -> factor','term',1,'p_term_factor','scalaSintactico.py',56),
  ('sentencia -> IF factor comparacion factor LBRACE cuerpo RBRACE','sentencia',7,'p_sentencia_if','scalaSintactico.py',60),
  ('comparacion -> GT','comparacion',1,'p_comparacion','scalaSintactico.py',64),
  ('comparacion -> GE','comparacion',1,'p_comparacion','scalaSintactico.py',65),
  ('comparacion -> LT','comparacion',1,'p_comparacion','scalaSintactico.py',66),
  ('comparacion -> LE','comparacion',1,'p_comparacion','scalaSintactico.py',67),
  ('comparacion -> EQUAL2','comparacion',1,'p_comparacion','scalaSintactico.py',68),
  ('factor -> INT_NUMBER','factor',1,'p_factor_int','scalaSintactico.py',71),
  ('factor -> DOUBLE_NUMBER','factor',1,'p_factor_double','scalaSintactico.py',74),
  ('booleano -> TRUE','booleano',1,'p_booleano','scalaSintactico.py',77),
  ('booleano -> FALSE','booleano',1,'p_booleano','scalaSintactico.py',78),
  ('string -> STRING','string',1,'p_string','scalaSintactico.py',81),
  ('double -> DOUBLE_NUMBER','double',1,'p_double','scalaSintactico.py',84),
  ('int -> INT_NUMBER','int',1,'p_int','scalaSintactico.py',87),
=======
  ("S' -> declararVariable","S'",1,None,None,None),
  ('declararVariable -> VAR ID COLON tipoValue','declararVariable',4,'p_declararVariable','scalaSintactico.py',9),
  ('declararVariable -> VAR ID COLON tipo','declararVariable',4,'p_declararVariable','scalaSintactico.py',10),
  ('declararVariable -> VAR ID EQUAL value','declararVariable',4,'p_declararVariable','scalaSintactico.py',11),
  ('declararVariable -> VAR ID EQUAL expression','declararVariable',4,'p_declararVariable','scalaSintactico.py',12),
  ('value -> string','value',1,'p_value','scalaSintactico.py',15),
  ('value -> booleano','value',1,'p_value','scalaSintactico.py',16),
  ('value -> NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',17),
  ('value -> NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',18),
  ('value -> NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',19),
  ('value -> NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',20),
  ('value -> ARRAY LPAREN elementosInternos RPAREN','value',4,'p_value','scalaSintactico.py',21),
  ('elementosInternos -> elementosInternosInt','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',24),
  ('elementosInternos -> elementosInternosDouble','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',25),
  ('elementosInternos -> elementosInternosBool','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',26),
  ('elementosInternos -> elementosInternosString','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',27),
  ('elementosInternosInt -> int','elementosInternosInt',1,'p_elementosInternosInt','scalaSintactico.py',30),
  ('elementosInternosInt -> int COMMA elementosInternosInt','elementosInternosInt',3,'p_elementosInternosInt','scalaSintactico.py',31),
  ('elementosInternosDouble -> double','elementosInternosDouble',1,'p_elementosInternosDouble','scalaSintactico.py',34),
  ('elementosInternosDouble -> double COMMA elementosInternosDouble','elementosInternosDouble',3,'p_elementosInternosDouble','scalaSintactico.py',35),
  ('elementosInternosBool -> booleano','elementosInternosBool',1,'p_elementosInternosBool','scalaSintactico.py',38),
  ('elementosInternosBool -> booleano COMMA elementosInternosBool','elementosInternosBool',3,'p_elementosInternosBool','scalaSintactico.py',39),
  ('elementosInternosString -> string','elementosInternosString',1,'p_elementosInternosString','scalaSintactico.py',42),
  ('elementosInternosString -> string COMMA elementosInternosString','elementosInternosString',3,'p_elementosInternosString','scalaSintactico.py',43),
  ('tipo -> INT','tipo',1,'p_tipo','scalaSintactico.py',46),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','scalaSintactico.py',47),
  ('tipo -> BOOL','tipo',1,'p_tipo','scalaSintactico.py',48),
  ('tipo -> STRING_TYPE','tipo',1,'p_tipo','scalaSintactico.py',49),
  ('tipoValue -> STRING_TYPE EQUAL string','tipoValue',3,'p_tipoValue','scalaSintactico.py',52),
  ('tipoValue -> BOOL EQUAL booleano','tipoValue',3,'p_tipoValue','scalaSintactico.py',53),
  ('tipoValue -> INT EQUAL int','tipoValue',3,'p_tipoValue','scalaSintactico.py',54),
  ('tipoValue -> DOUBLE EQUAL double','tipoValue',3,'p_tipoValue','scalaSintactico.py',55),
  ('tipoValue -> ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',56),
  ('tipoValue -> ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',57),
  ('tipoValue -> ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',58),
  ('tipoValue -> ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',59),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','scalaSintactico.py',62),
  ('cuerpo -> sentencia','cuerpo',1,'p_cuerpo','scalaSintactico.py',63),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','scalaSintactico.py',66),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','scalaSintactico.py',70),
  ('expression -> term','expression',1,'p_expression_term','scalaSintactico.py',74),
  ('term -> term TIMES factor','term',3,'p_term_times','scalaSintactico.py',78),
  ('term -> term DIVIDE factor','term',3,'p_term_div','scalaSintactico.py',82),
  ('term -> factor','term',1,'p_term_factor','scalaSintactico.py',86),
  ('sentencia -> IF factor comparacion factor LBRACE cuerpo RBRACE','sentencia',7,'p_sentencia_if','scalaSintactico.py',90),
  ('comparacion -> GT','comparacion',1,'p_comparacion','scalaSintactico.py',94),
  ('comparacion -> GE','comparacion',1,'p_comparacion','scalaSintactico.py',95),
  ('comparacion -> LT','comparacion',1,'p_comparacion','scalaSintactico.py',96),
  ('comparacion -> LE','comparacion',1,'p_comparacion','scalaSintactico.py',97),
  ('factor -> INT_NUMBER','factor',1,'p_factor_int','scalaSintactico.py',100),
  ('factor -> DOUBLE_NUMBER','factor',1,'p_factor_double','scalaSintactico.py',103),
  ('booleano -> TRUE','booleano',1,'p_booleano','scalaSintactico.py',106),
  ('booleano -> FALSE','booleano',1,'p_booleano','scalaSintactico.py',107),
  ('string -> STRING','string',1,'p_string','scalaSintactico.py',110),
  ('double -> DOUBLE_NUMBER','double',1,'p_double','scalaSintactico.py',113),
  ('int -> INT_NUMBER','int',1,'p_int','scalaSintactico.py',116),
>>>>>>> 2fcbf43bc68c3329114fcf4778e5f075909bc071
]
