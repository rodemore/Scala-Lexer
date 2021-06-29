
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARRAY BOOL CLASS COLON COMMA DECREMENT DEF DIVIDE DOT DOUBLE DOUBLE_NUMBER ELSE EQ EQUAL EQUAL2 EQUALS FALSE FOR GE GT HEAD ID IF INCREMENT INT INT_NUMBER ISEMPTY LBRACE LBRACK LE LENGTH LIST LPAREN LT MINUS MOD NEW OBJECT PLUS PRINTLN PRODUCTITERATOR RBRACE RBRACK RETURN REVERSE RPAREN SEMICOLON STRING STRING_TYPE SWAP TAIL THIS TIMES TOSTRING TRUE VAL VAR WHILE unitcuerpo : expression\n             | sentencia\n             | declararVariable\n             | declararConstante\n             | funcionesTupladeclararConstante : VAL ID COLON tipoValueCons\n                        | VAL ID COLON tipo\n                        | VAL ID EQUAL valueCons\n                        | VAL ID EQUAL expressiondeclararVariable : VAR ID COLON tipoValue\n                        | VAR ID COLON tipo\n                        | VAR ID EQUAL value\n                        | VAR ID EQUAL expressionvalue : string\n            | booleano\n            | NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN\n            | ARRAY LPAREN elementosInternos RPARENelementosInternos : elementosInternosInt\n            | elementosInternosDouble\n            | elementosInternosBool\n            | elementosInternosStringelementosInternosInt : int\n            | int COMMA elementosInternosIntelementosInternosDouble : double\n            | double COMMA elementosInternosDoubleelementosInternosBool : booleano\n            | booleano COMMA elementosInternosBoolelementosInternosString : string\n            | string COMMA elementosInternosStringelementosInternos2 : int\n            | double\n            | booleano\n            | string\n            | int COMMA elementosInternos2\n            | double COMMA elementosInternos2\n            | booleano COMMA elementosInternos2\n            | string COMMA elementosInternos2valueCons : string\n            | booleano\n            | tuplatipo : INT\n             | DOUBLE\n             | BOOL\n             | STRING_TYPEtipoValue : STRING_TYPE EQUAL string\n                | BOOL EQUAL booleano\n                | INT EQUAL int\n                | DOUBLE EQUAL double\n                | ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPARENtipoValueCons : STRING_TYPE EQUAL string\n                | BOOL EQUAL booleano\n                | INT EQUAL int\n                | DOUBLE EQUAL doubletupla : LPAREN elementosInternos2 RPARENfuncionesTupla : tuplaSwap\n                | tuplaToString\n                | tuplaProductIteratortuplaSwap : ID DOT SWAPtuplaToString : ID DOT TOSTRINGtuplaProductIterator : ID DOT PRODUCTITERATORfuncionesArray : arrayHead\n            | arrayTail\n            | arrayLengtharrayHead : ID DOT HEADarrayTail : ID DOT TAILarrayLength : ID DOT LENGTHexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorsentencia : IF factor comparacion factor LBRACE cuerpo RBRACEcomparacion : GT\n                    | GE\n                    | LT\n                    | LE\n                    | EQUAL2factor : INT_NUMBERfactor : DOUBLE_NUMBERbooleano : TRUE\n                | FALSEstring : STRINGdouble : DOUBLE_NUMBERint : INT_NUMBER'
    
_lr_action_items = {'IF':([0,72,],[8,8,]),'VAR':([0,72,],[10,10,]),'VAL':([0,72,],[12,12,]),'ID':([0,10,12,72,],[11,23,25,11,]),'INT_NUMBER':([0,8,18,19,20,21,30,31,32,33,34,35,37,42,71,72,75,79,82,115,116,117,118,129,153,154,155,156,181,182,183,184,],[16,16,16,16,16,16,16,-80,-81,-82,-83,-84,16,16,89,16,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'DOUBLE_NUMBER':([0,8,18,19,20,21,30,31,32,33,34,35,37,42,71,72,76,79,83,115,116,117,118,130,],[17,17,17,17,17,17,17,-80,-81,-82,-83,-84,17,17,90,17,90,90,90,90,90,90,90,90,]),'$end':([1,2,3,4,5,6,7,9,13,14,15,16,17,26,27,28,29,38,39,40,44,45,46,47,48,49,51,52,53,54,57,58,59,60,61,62,63,64,65,66,67,68,69,70,89,90,92,93,94,95,110,111,112,113,114,119,128,169,170,171,172,189,190,191,192,],[0,-1,-2,-3,-4,-5,-75,-78,-61,-62,-63,-85,-86,-73,-74,-76,-77,-64,-65,-66,-10,-11,-47,-46,-44,-45,-12,-13,-14,-15,-89,-87,-88,-6,-7,-47,-46,-44,-45,-8,-9,-41,-42,-43,-91,-90,-48,-49,-50,-51,-56,-57,-58,-59,-60,-79,-20,-16,-17,-18,-19,-52,-53,-54,-55,]),'RBRACE':([2,3,4,5,6,7,9,13,14,15,16,17,26,27,28,29,38,39,40,44,45,46,47,48,49,51,52,53,54,57,58,59,60,61,62,63,64,65,66,67,68,69,70,89,90,91,92,93,94,95,110,111,112,113,114,119,128,169,170,171,172,189,190,191,192,],[-1,-2,-3,-4,-5,-75,-78,-61,-62,-63,-85,-86,-73,-74,-76,-77,-64,-65,-66,-10,-11,-47,-46,-44,-45,-12,-13,-14,-15,-89,-87,-88,-6,-7,-47,-46,-44,-45,-8,-9,-41,-42,-43,-91,-90,119,-48,-49,-50,-51,-56,-57,-58,-59,-60,-79,-20,-16,-17,-18,-19,-52,-53,-54,-55,]),'PLUS':([2,7,9,16,17,26,27,28,29,52,67,],[18,-75,-78,-85,-86,-73,-74,-76,-77,18,18,]),'MINUS':([2,7,9,16,17,26,27,28,29,52,67,],[19,-75,-78,-85,-86,-73,-74,-76,-77,19,19,]),'TIMES':([7,9,16,17,26,27,28,29,],[20,-78,-85,-86,20,20,-76,-77,]),'DIVIDE':([7,9,16,17,26,27,28,29,],[21,-78,-85,-86,21,21,-76,-77,]),'DOT':([11,],[24,]),'GT':([16,17,22,],[-85,-86,31,]),'GE':([16,17,22,],[-85,-86,32,]),'LT':([16,17,22,],[-85,-86,33,]),'LE':([16,17,22,],[-85,-86,34,]),'EQUAL2':([16,17,22,],[-85,-86,35,]),'LBRACE':([16,17,43,],[-85,-86,72,]),'COLON':([23,25,],[36,41,]),'EQUAL':([23,25,46,47,48,49,62,63,64,65,120,121,122,123,],[37,42,73,74,75,76,80,81,82,83,137,138,139,140,]),'SWAP':([24,],[38,]),'TOSTRING':([24,],[39,]),'PRODUCTITERATOR':([24,],[40,]),'STRING_TYPE':([36,41,77,100,168,],[46,62,99,127,176,]),'BOOL':([36,41,77,100,167,],[47,63,98,126,175,]),'INT':([36,41,77,100,165,],[48,64,96,124,173,]),'DOUBLE':([36,41,77,100,166,],[49,65,97,125,174,]),'ARRAY':([36,37,55,149,150,151,152,],[50,56,78,157,158,159,160,]),'NEW':([37,137,138,139,140,],[55,149,150,151,152,]),'STRING':([37,42,71,73,79,80,115,116,117,118,132,],[57,57,57,57,57,57,57,57,57,57,57,]),'TRUE':([37,42,71,74,79,81,115,116,117,118,131,],[58,58,58,58,58,58,58,58,58,58,58,]),'FALSE':([37,42,71,74,79,81,115,116,117,118,131,],[59,59,59,59,59,59,59,59,59,59,59,]),'LPAREN':([42,56,141,142,143,144,177,178,179,180,],[71,79,153,154,155,156,181,182,183,184,]),'LBRACK':([50,78,157,158,159,160,],[77,100,165,166,167,168,]),'COMMA':([57,58,59,85,86,87,88,89,90,106,107,108,109,],[-89,-87,-88,115,116,117,118,-91,-90,129,130,131,132,]),'RPAREN':([57,58,59,84,85,86,87,88,89,90,101,102,103,104,105,106,107,108,109,133,134,135,136,145,146,147,148,161,162,163,164,185,186,187,188,],[-89,-87,-88,114,-33,-34,-35,-36,-91,-90,128,-21,-22,-23,-24,-25,-27,-29,-31,-37,-38,-39,-40,-26,-28,-30,-32,169,170,171,172,189,190,191,192,]),'RBRACK':([96,97,98,99,124,125,126,127,173,174,175,176,],[120,121,122,123,141,142,143,144,177,178,179,180,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,72,],[1,91,]),'expression':([0,37,42,72,],[2,52,67,2,]),'sentencia':([0,72,],[3,3,]),'declararVariable':([0,72,],[4,4,]),'declararConstante':([0,72,],[5,5,]),'funcionesTupla':([0,72,],[6,6,]),'term':([0,18,19,37,42,72,],[7,26,27,7,7,7,]),'factor':([0,8,18,19,20,21,30,37,42,72,],[9,22,9,9,28,29,43,9,9,9,]),'tuplaSwap':([0,72,],[13,13,]),'tuplaToString':([0,72,],[14,14,]),'tuplaProductIterator':([0,72,],[15,15,]),'comparacion':([22,],[30,]),'tipoValue':([36,],[44,]),'tipo':([36,41,],[45,61,]),'value':([37,],[51,]),'string':([37,42,71,73,79,80,115,116,117,118,132,],[53,68,88,92,109,110,88,88,88,88,109,]),'booleano':([37,42,71,74,79,81,115,116,117,118,131,],[54,69,87,93,108,111,87,87,87,87,108,]),'tipoValueCons':([41,],[60,]),'valueCons':([42,],[66,]),'tupla':([42,],[70,]),'elementosInternos2':([71,115,116,117,118,],[84,133,134,135,136,]),'int':([71,75,79,82,115,116,117,118,129,153,154,155,156,181,182,183,184,],[85,94,106,112,85,85,85,85,106,161,162,163,164,185,186,187,188,]),'double':([71,76,79,83,115,116,117,118,130,],[86,95,107,113,86,86,86,86,107,]),'elementosInternos':([79,],[101,]),'elementosInternosInt':([79,129,],[102,145,]),'elementosInternosDouble':([79,130,],[103,146,]),'elementosInternosBool':([79,131,],[104,147,]),'elementosInternosString':([79,132,],[105,148,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','scalaSintactico.py',14),
  ('cuerpo -> sentencia','cuerpo',1,'p_cuerpo','scalaSintactico.py',15),
  ('cuerpo -> declararVariable','cuerpo',1,'p_cuerpo','scalaSintactico.py',16),
  ('cuerpo -> declararConstante','cuerpo',1,'p_cuerpo','scalaSintactico.py',17),
  ('cuerpo -> funcionesTupla','cuerpo',1,'p_cuerpo','scalaSintactico.py',18),
  ('declararConstante -> VAL ID COLON tipoValueCons','declararConstante',4,'p_declararConstante','scalaSintactico.py',21),
  ('declararConstante -> VAL ID COLON tipo','declararConstante',4,'p_declararConstante','scalaSintactico.py',22),
  ('declararConstante -> VAL ID EQUAL valueCons','declararConstante',4,'p_declararConstante','scalaSintactico.py',23),
  ('declararConstante -> VAL ID EQUAL expression','declararConstante',4,'p_declararConstante','scalaSintactico.py',24),
  ('declararVariable -> VAR ID COLON tipoValue','declararVariable',4,'p_declararVariable','scalaSintactico.py',27),
  ('declararVariable -> VAR ID COLON tipo','declararVariable',4,'p_declararVariable','scalaSintactico.py',28),
  ('declararVariable -> VAR ID EQUAL value','declararVariable',4,'p_declararVariable','scalaSintactico.py',29),
  ('declararVariable -> VAR ID EQUAL expression','declararVariable',4,'p_declararVariable','scalaSintactico.py',30),
  ('value -> string','value',1,'p_value','scalaSintactico.py',33),
  ('value -> booleano','value',1,'p_value','scalaSintactico.py',34),
  ('value -> NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',35),
  ('value -> NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',36),
  ('value -> NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',37),
  ('value -> NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',38),
  ('value -> ARRAY LPAREN elementosInternos RPAREN','value',4,'p_value','scalaSintactico.py',39),
  ('elementosInternos -> elementosInternosInt','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',42),
  ('elementosInternos -> elementosInternosDouble','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',43),
  ('elementosInternos -> elementosInternosBool','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',44),
  ('elementosInternos -> elementosInternosString','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',45),
  ('elementosInternosInt -> int','elementosInternosInt',1,'p_elementosInternosInt','scalaSintactico.py',48),
  ('elementosInternosInt -> int COMMA elementosInternosInt','elementosInternosInt',3,'p_elementosInternosInt','scalaSintactico.py',49),
  ('elementosInternosDouble -> double','elementosInternosDouble',1,'p_elementosInternosDouble','scalaSintactico.py',52),
  ('elementosInternosDouble -> double COMMA elementosInternosDouble','elementosInternosDouble',3,'p_elementosInternosDouble','scalaSintactico.py',53),
  ('elementosInternosBool -> booleano','elementosInternosBool',1,'p_elementosInternosBool','scalaSintactico.py',56),
  ('elementosInternosBool -> booleano COMMA elementosInternosBool','elementosInternosBool',3,'p_elementosInternosBool','scalaSintactico.py',57),
  ('elementosInternosString -> string','elementosInternosString',1,'p_elementosInternosString','scalaSintactico.py',60),
  ('elementosInternosString -> string COMMA elementosInternosString','elementosInternosString',3,'p_elementosInternosString','scalaSintactico.py',61),
  ('elementosInternos2 -> int','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',64),
  ('elementosInternos2 -> double','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',65),
  ('elementosInternos2 -> booleano','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',66),
  ('elementosInternos2 -> string','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',67),
  ('elementosInternos2 -> int COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',68),
  ('elementosInternos2 -> double COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',69),
  ('elementosInternos2 -> booleano COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',70),
  ('elementosInternos2 -> string COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',71),
  ('valueCons -> string','valueCons',1,'p_valueCons','scalaSintactico.py',74),
  ('valueCons -> booleano','valueCons',1,'p_valueCons','scalaSintactico.py',75),
  ('valueCons -> tupla','valueCons',1,'p_valueCons','scalaSintactico.py',76),
  ('tipo -> INT','tipo',1,'p_tipo','scalaSintactico.py',79),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','scalaSintactico.py',80),
  ('tipo -> BOOL','tipo',1,'p_tipo','scalaSintactico.py',81),
  ('tipo -> STRING_TYPE','tipo',1,'p_tipo','scalaSintactico.py',82),
  ('tipoValue -> STRING_TYPE EQUAL string','tipoValue',3,'p_tipoValue','scalaSintactico.py',85),
  ('tipoValue -> BOOL EQUAL booleano','tipoValue',3,'p_tipoValue','scalaSintactico.py',86),
  ('tipoValue -> INT EQUAL int','tipoValue',3,'p_tipoValue','scalaSintactico.py',87),
  ('tipoValue -> DOUBLE EQUAL double','tipoValue',3,'p_tipoValue','scalaSintactico.py',88),
  ('tipoValue -> ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',89),
  ('tipoValue -> ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',90),
  ('tipoValue -> ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',91),
  ('tipoValue -> ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',92),
  ('tipoValueCons -> STRING_TYPE EQUAL string','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',95),
  ('tipoValueCons -> BOOL EQUAL booleano','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',96),
  ('tipoValueCons -> INT EQUAL int','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',97),
  ('tipoValueCons -> DOUBLE EQUAL double','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',98),
  ('tupla -> LPAREN elementosInternos2 RPAREN','tupla',3,'p_tupla','scalaSintactico.py',101),
  ('funcionesTupla -> tuplaSwap','funcionesTupla',1,'p_funcionesTupla','scalaSintactico.py',104),
  ('funcionesTupla -> tuplaToString','funcionesTupla',1,'p_funcionesTupla','scalaSintactico.py',105),
  ('funcionesTupla -> tuplaProductIterator','funcionesTupla',1,'p_funcionesTupla','scalaSintactico.py',106),
  ('tuplaSwap -> ID DOT SWAP','tuplaSwap',3,'p_tuplaSwap','scalaSintactico.py',109),
  ('tuplaToString -> ID DOT TOSTRING','tuplaToString',3,'p_tuplaToString','scalaSintactico.py',112),
  ('tuplaProductIterator -> ID DOT PRODUCTITERATOR','tuplaProductIterator',3,'p_tuplaProductIterator','scalaSintactico.py',115),
  ('funcionesArray -> arrayHead','funcionesArray',1,'p_funcionesArray','scalaSintactico.py',118),
  ('funcionesArray -> arrayTail','funcionesArray',1,'p_funcionesArray','scalaSintactico.py',119),
  ('funcionesArray -> arrayLength','funcionesArray',1,'p_funcionesArray','scalaSintactico.py',120),
  ('arrayHead -> ID DOT HEAD','arrayHead',3,'p_arrayHead','scalaSintactico.py',123),
  ('arrayTail -> ID DOT TAIL','arrayTail',3,'p_arrayTail','scalaSintactico.py',126),
  ('arrayLength -> ID DOT LENGTH','arrayLength',3,'p_arrayLength','scalaSintactico.py',129),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','scalaSintactico.py',132),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','scalaSintactico.py',136),
  ('expression -> term','expression',1,'p_expression_term','scalaSintactico.py',140),
  ('term -> term TIMES factor','term',3,'p_term_times','scalaSintactico.py',144),
  ('term -> term DIVIDE factor','term',3,'p_term_div','scalaSintactico.py',148),
  ('term -> factor','term',1,'p_term_factor','scalaSintactico.py',152),
  ('sentencia -> IF factor comparacion factor LBRACE cuerpo RBRACE','sentencia',7,'p_sentencia_if','scalaSintactico.py',156),
  ('comparacion -> GT','comparacion',1,'p_comparacion','scalaSintactico.py',160),
  ('comparacion -> GE','comparacion',1,'p_comparacion','scalaSintactico.py',161),
  ('comparacion -> LT','comparacion',1,'p_comparacion','scalaSintactico.py',162),
  ('comparacion -> LE','comparacion',1,'p_comparacion','scalaSintactico.py',163),
  ('comparacion -> EQUAL2','comparacion',1,'p_comparacion','scalaSintactico.py',164),
  ('factor -> INT_NUMBER','factor',1,'p_factor_int','scalaSintactico.py',167),
  ('factor -> DOUBLE_NUMBER','factor',1,'p_factor_double','scalaSintactico.py',170),
  ('booleano -> TRUE','booleano',1,'p_booleano','scalaSintactico.py',173),
  ('booleano -> FALSE','booleano',1,'p_booleano','scalaSintactico.py',174),
  ('string -> STRING','string',1,'p_string','scalaSintactico.py',177),
  ('double -> DOUBLE_NUMBER','double',1,'p_double','scalaSintactico.py',180),
  ('int -> INT_NUMBER','int',1,'p_int','scalaSintactico.py',183),
]
