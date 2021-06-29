
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARRAY BOOL CLASS COLON COMMA DECREMENT DEF DIVIDE DOT DOUBLE DOUBLE_NUMBER ELSE EQ EQUAL EQUAL2 EQUALS FALSE FOR GE GT HEAD ID IF INCREMENT INPUT INT INT_NUMBER ISEMPTY LBRACE LBRACK LE LENGTH LIST LM LPAREN LT MINUS MOD NEW OBJECT PLUS PRINTLN PRODUCTITERATOR RBRACE RBRACK RETURN REVERSE RPAREN SEMICOLON STRING STRING_TYPE SWAP TAIL THIS TIMES TOSTRING TRUE VAL VAR WHILE unitcuerpo : expression\n             | sentencia\n             | declararVariable\n             | declararConstante\n             | funcionesTupla\n             | funcionesArray\n             | for\n             | funcionesPropias\n             | comparacionesVardeclararConstante : VAL ID COLON tipoValueCons\n                        | VAL ID COLON tipo\n                        | VAL ID EQUAL valueCons\n                        | VAL ID EQUAL expressiondeclararVariable : VAR ID COLON tipoValue\n                        | VAR ID COLON tipo\n                        | VAR ID EQUAL value\n                        | VAR ID EQUAL expressionvalue : string\n            | booleano\n            | NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN\n            | NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN\n            | ARRAY LPAREN elementosInternos RPAREN\n            | LIST LPAREN elementosInternos RPARENelementosInternos : elementosInternosInt\n            | elementosInternosDouble\n            | elementosInternosBool\n            | elementosInternosStringelementosInternosInt : int\n            | int COMMA elementosInternosIntelementosInternosDouble : double\n            | double COMMA elementosInternosDoubleelementosInternosBool : booleano\n            | booleano COMMA elementosInternosBoolelementosInternosString : string\n            | string COMMA elementosInternosStringelementosInternos2 : int\n            | double\n            | booleano\n            | string\n            | int COMMA elementosInternos2\n            | double COMMA elementosInternos2\n            | booleano COMMA elementosInternos2\n            | string COMMA elementosInternos2valueCons : string\n            | booleano\n            | tuplatipo : INT\n             | DOUBLE\n             | BOOL\n             | STRING_TYPEtipoValue : STRING_TYPE EQUAL string\n                | BOOL EQUAL booleano\n                | INT EQUAL int\n                | DOUBLE EQUAL double\n                | ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN\n                | ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN\n                | LIST LBRACK INT RBRACK EQUAL LIST LPAREN elementosInternos RPAREN\n                | LIST LBRACK DOUBLE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN\n                | LIST LBRACK BOOL RBRACK EQUAL LIST LPAREN elementosInternos RPAREN\n                | LIST LBRACK STRING_TYPE RBRACK EQUAL LIST LPAREN elementosInternos RPARENtipoValueCons : STRING_TYPE EQUAL string\n                | BOOL EQUAL booleano\n                | INT EQUAL int\n                | DOUBLE EQUAL doubletupla : LPAREN elementosInternos2 RPARENfuncionesTupla : tuplaSwap\n                | tuplaToString\n                | tuplaProductIteratortuplaSwap : ID DOT SWAPtuplaToString : ID DOT TOSTRING LPAREN RPARENtuplaProductIterator : ID DOT PRODUCTITERATORfuncionesArray : arrayHead\n            | arrayTail\n            | arrayLengthfuncionesPropias : INPUT LPAREN RPAREN\n            | PRINTLN LPAREN string RPAREN\n            | PRINTLN LPAREN booleano RPAREN\n            | PRINTLN LPAREN ID RPAREN\n            | PRINTLN LPAREN expression RPARENarrayHead : ID DOT HEADarrayTail : ID DOT TAILarrayLength : ID DOT LENGTHexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorsentencia : IF factor comparacion factor LBRACE cuerpo RBRACEfor : FOR LPAREN ID LM ID RPAREN LBRACE  cuerpo  RBRACEcomparacionesVar : ID DOT EQUALS LPAREN ID  RPAREN\n                        | ID DOT EQ LPAREN ID RPARENcomparacion : GT\n                    | GE\n                    | LT\n                    | LE\n                    | EQUAL2factor : intfactor : doublebooleano : TRUE\n                | FALSEstring : STRINGdouble : DOUBLE_NUMBERint : INT_NUMBER'
    
_lr_action_items = {'IF':([0,108,190,],[12,12,12,]),'VAR':([0,108,190,],[14,14,14,]),'VAL':([0,108,190,],[16,16,16,]),'FOR':([0,108,190,],[23,23,23,]),'INPUT':([0,108,190,],[24,24,24,]),'PRINTLN':([0,108,190,],[25,25,25,]),'ID':([0,14,16,38,40,88,89,103,108,190,],[15,35,37,63,67,118,119,130,15,15,]),'INT_NUMBER':([0,12,30,31,32,33,40,45,46,47,48,49,50,52,62,102,108,111,116,117,123,162,163,164,165,181,190,216,217,218,219,225,226,227,228,257,258,259,260,],[28,28,28,28,28,28,28,28,-97,-98,-99,-100,-101,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'DOUBLE_NUMBER':([0,12,30,31,32,33,40,45,46,47,48,49,50,52,62,102,108,112,116,117,124,162,163,164,165,182,190,225,226,227,228,],[29,29,29,29,29,29,29,29,-97,-98,-99,-100,-101,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,17,18,19,20,21,22,26,27,28,29,41,42,43,44,55,57,58,59,60,64,69,70,71,73,74,75,76,77,78,81,82,83,84,91,92,93,94,95,96,97,98,99,100,101,104,105,106,107,120,132,133,134,135,155,156,157,158,159,160,161,167,180,185,220,241,242,243,244,249,250,251,252,265,266,267,268,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-89,-92,-70,-71,-72,-76,-77,-78,-102,-103,-108,-107,-87,-88,-90,-91,-73,-75,-84,-85,-86,-79,-106,-104,-105,-14,-15,-52,-51,-49,-50,-16,-17,-18,-19,-10,-11,-52,-51,-49,-50,-12,-13,-46,-47,-48,-80,-81,-82,-83,-74,-53,-54,-55,-56,-95,-96,-65,-66,-67,-68,-69,-93,-24,-25,-94,-20,-21,-22,-23,-61,-62,-63,-64,-57,-58,-59,-60,]),'RBRACE':([2,3,4,5,6,7,8,9,10,11,13,17,18,19,20,21,22,26,27,28,29,41,42,43,44,55,57,58,59,60,64,69,70,71,73,74,75,76,77,78,81,82,83,84,91,92,93,94,95,96,97,98,99,100,101,104,105,106,107,120,131,132,133,134,135,155,156,157,158,159,160,161,167,180,185,207,220,241,242,243,244,249,250,251,252,265,266,267,268,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-89,-92,-70,-71,-72,-76,-77,-78,-102,-103,-108,-107,-87,-88,-90,-91,-73,-75,-84,-85,-86,-79,-106,-104,-105,-14,-15,-52,-51,-49,-50,-16,-17,-18,-19,-10,-11,-52,-51,-49,-50,-12,-13,-46,-47,-48,-80,-81,-82,-83,-74,167,-53,-54,-55,-56,-95,-96,-65,-66,-67,-68,-69,-93,-24,-25,220,-94,-20,-21,-22,-23,-61,-62,-63,-64,-57,-58,-59,-60,]),'PLUS':([2,11,13,26,27,28,29,41,42,43,44,68,82,98,],[30,-89,-92,-102,-103,-108,-107,-87,-88,-90,-91,30,30,30,]),'MINUS':([2,11,13,26,27,28,29,41,42,43,44,68,82,98,],[31,-89,-92,-102,-103,-108,-107,-87,-88,-90,-91,31,31,31,]),'RPAREN':([11,13,26,27,28,29,39,41,42,43,44,65,66,67,68,69,70,71,90,118,119,125,126,127,128,129,130,145,146,147,148,149,150,151,152,153,154,186,187,188,189,203,204,205,206,229,230,231,232,237,238,239,240,261,262,263,264,],[-89,-92,-102,-103,-108,-107,64,-87,-88,-90,-91,104,105,106,107,-106,-104,-105,120,155,156,161,-38,-39,-40,-41,166,180,-26,-27,-28,-29,-30,-32,-34,-36,185,-42,-43,-44,-45,-31,-33,-35,-37,241,242,243,244,249,250,251,252,265,266,267,268,]),'TIMES':([11,13,26,27,28,29,41,42,43,44,],[32,-92,-102,-103,-108,-107,32,32,-90,-91,]),'DIVIDE':([11,13,26,27,28,29,41,42,43,44,],[33,-92,-102,-103,-108,-107,33,33,-90,-91,]),'DOT':([15,],[36,]),'LPAREN':([23,24,25,53,54,56,62,86,87,199,200,201,202,212,213,214,215,253,254,255,256,],[38,39,40,88,89,90,102,116,117,216,217,218,219,225,226,227,228,257,258,259,260,]),'GT':([26,27,28,29,34,],[-102,-103,-108,-107,46,]),'GE':([26,27,28,29,34,],[-102,-103,-108,-107,47,]),'LT':([26,27,28,29,34,],[-102,-103,-108,-107,48,]),'LE':([26,27,28,29,34,],[-102,-103,-108,-107,49,]),'EQUAL2':([26,27,28,29,34,],[-102,-103,-108,-107,50,]),'LBRACE':([26,27,28,29,72,166,],[-102,-103,-108,-107,108,190,]),'COMMA':([28,29,69,70,71,126,127,128,129,150,151,152,153,],[-108,-107,-106,-104,-105,162,163,164,165,181,182,183,184,]),'COLON':([35,37,],[51,61,]),'EQUAL':([35,37,75,76,77,78,93,94,95,96,168,169,170,171,172,173,174,175,],[52,62,109,110,111,112,121,122,123,124,191,192,193,194,195,196,197,198,]),'EQUALS':([36,],[53,]),'EQ':([36,],[54,]),'SWAP':([36,],[55,]),'TOSTRING':([36,],[56,]),'PRODUCTITERATOR':([36,],[57,]),'HEAD':([36,],[58,]),'TAIL':([36,],[59,]),'LENGTH':([36,],[60,]),'STRING':([40,52,62,102,109,116,117,121,162,163,164,165,184,225,226,227,228,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'TRUE':([40,52,62,102,110,116,117,122,162,163,164,165,183,225,226,227,228,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'FALSE':([40,52,62,102,110,116,117,122,162,163,164,165,183,225,226,227,228,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'STRING_TYPE':([51,61,113,114,144,236,],[75,93,139,143,179,248,]),'BOOL':([51,61,113,114,144,235,],[76,94,138,142,178,247,]),'INT':([51,61,113,114,144,233,],[77,95,136,140,176,245,]),'DOUBLE':([51,61,113,114,144,234,],[78,96,137,141,177,246,]),'ARRAY':([51,52,85,208,209,210,211,],[79,86,115,221,222,223,224,]),'LIST':([51,52,195,196,197,198,],[80,87,212,213,214,215,]),'NEW':([52,191,192,193,194,],[85,208,209,210,211,]),'LM':([63,],[103,]),'LBRACK':([79,80,115,221,222,223,224,],[113,114,144,233,234,235,236,]),'RBRACK':([136,137,138,139,140,141,142,143,176,177,178,179,245,246,247,248,],[168,169,170,171,172,173,174,175,199,200,201,202,253,254,255,256,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,108,190,],[1,131,207,]),'expression':([0,40,52,62,108,190,],[2,68,82,98,2,2,]),'sentencia':([0,108,190,],[3,3,3,]),'declararVariable':([0,108,190,],[4,4,4,]),'declararConstante':([0,108,190,],[5,5,5,]),'funcionesTupla':([0,108,190,],[6,6,6,]),'funcionesArray':([0,108,190,],[7,7,7,]),'for':([0,108,190,],[8,8,8,]),'funcionesPropias':([0,108,190,],[9,9,9,]),'comparacionesVar':([0,108,190,],[10,10,10,]),'term':([0,30,31,40,52,62,108,190,],[11,41,42,11,11,11,11,11,]),'factor':([0,12,30,31,32,33,40,45,52,62,108,190,],[13,34,13,13,43,44,13,72,13,13,13,13,]),'tuplaSwap':([0,108,190,],[17,17,17,]),'tuplaToString':([0,108,190,],[18,18,18,]),'tuplaProductIterator':([0,108,190,],[19,19,19,]),'arrayHead':([0,108,190,],[20,20,20,]),'arrayTail':([0,108,190,],[21,21,21,]),'arrayLength':([0,108,190,],[22,22,22,]),'int':([0,12,30,31,32,33,40,45,52,62,102,108,111,116,117,123,162,163,164,165,181,190,216,217,218,219,225,226,227,228,257,258,259,260,],[26,26,26,26,26,26,26,26,26,26,126,26,134,150,150,159,126,126,126,126,150,26,229,230,231,232,150,150,150,150,261,262,263,264,]),'double':([0,12,30,31,32,33,40,45,52,62,102,108,112,116,117,124,162,163,164,165,182,190,225,226,227,228,],[27,27,27,27,27,27,27,27,27,27,127,27,135,151,151,160,127,127,127,127,151,27,151,151,151,151,]),'comparacion':([34,],[45,]),'string':([40,52,62,102,109,116,117,121,162,163,164,165,184,225,226,227,228,],[65,83,99,129,132,153,153,157,129,129,129,129,153,153,153,153,153,]),'booleano':([40,52,62,102,110,116,117,122,162,163,164,165,183,225,226,227,228,],[66,84,100,128,133,152,152,158,128,128,128,128,152,152,152,152,152,]),'tipoValue':([51,],[73,]),'tipo':([51,61,],[74,92,]),'value':([52,],[81,]),'tipoValueCons':([61,],[91,]),'valueCons':([62,],[97,]),'tupla':([62,],[101,]),'elementosInternos2':([102,162,163,164,165,],[125,186,187,188,189,]),'elementosInternos':([116,117,225,226,227,228,],[145,154,237,238,239,240,]),'elementosInternosInt':([116,117,181,225,226,227,228,],[146,146,203,146,146,146,146,]),'elementosInternosDouble':([116,117,182,225,226,227,228,],[147,147,204,147,147,147,147,]),'elementosInternosBool':([116,117,183,225,226,227,228,],[148,148,205,148,148,148,148,]),'elementosInternosString':([116,117,184,225,226,227,228,],[149,149,206,149,149,149,149,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','scalaSintactico.py',8),
  ('cuerpo -> sentencia','cuerpo',1,'p_cuerpo','scalaSintactico.py',9),
  ('cuerpo -> declararVariable','cuerpo',1,'p_cuerpo','scalaSintactico.py',10),
  ('cuerpo -> declararConstante','cuerpo',1,'p_cuerpo','scalaSintactico.py',11),
  ('cuerpo -> funcionesTupla','cuerpo',1,'p_cuerpo','scalaSintactico.py',12),
  ('cuerpo -> funcionesArray','cuerpo',1,'p_cuerpo','scalaSintactico.py',13),
  ('cuerpo -> for','cuerpo',1,'p_cuerpo','scalaSintactico.py',14),
  ('cuerpo -> funcionesPropias','cuerpo',1,'p_cuerpo','scalaSintactico.py',15),
  ('cuerpo -> comparacionesVar','cuerpo',1,'p_cuerpo','scalaSintactico.py',16),
  ('declararConstante -> VAL ID COLON tipoValueCons','declararConstante',4,'p_declararConstante','scalaSintactico.py',19),
  ('declararConstante -> VAL ID COLON tipo','declararConstante',4,'p_declararConstante','scalaSintactico.py',20),
  ('declararConstante -> VAL ID EQUAL valueCons','declararConstante',4,'p_declararConstante','scalaSintactico.py',21),
  ('declararConstante -> VAL ID EQUAL expression','declararConstante',4,'p_declararConstante','scalaSintactico.py',22),
  ('declararVariable -> VAR ID COLON tipoValue','declararVariable',4,'p_declararVariable','scalaSintactico.py',25),
  ('declararVariable -> VAR ID COLON tipo','declararVariable',4,'p_declararVariable','scalaSintactico.py',26),
  ('declararVariable -> VAR ID EQUAL value','declararVariable',4,'p_declararVariable','scalaSintactico.py',27),
  ('declararVariable -> VAR ID EQUAL expression','declararVariable',4,'p_declararVariable','scalaSintactico.py',28),
  ('value -> string','value',1,'p_value','scalaSintactico.py',31),
  ('value -> booleano','value',1,'p_value','scalaSintactico.py',32),
  ('value -> NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',33),
  ('value -> NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',34),
  ('value -> NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',35),
  ('value -> NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN','value',8,'p_value','scalaSintactico.py',36),
  ('value -> ARRAY LPAREN elementosInternos RPAREN','value',4,'p_value','scalaSintactico.py',37),
  ('value -> LIST LPAREN elementosInternos RPAREN','value',4,'p_value','scalaSintactico.py',38),
  ('elementosInternos -> elementosInternosInt','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',41),
  ('elementosInternos -> elementosInternosDouble','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',42),
  ('elementosInternos -> elementosInternosBool','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',43),
  ('elementosInternos -> elementosInternosString','elementosInternos',1,'p_elementosInternos','scalaSintactico.py',44),
  ('elementosInternosInt -> int','elementosInternosInt',1,'p_elementosInternosInt','scalaSintactico.py',47),
  ('elementosInternosInt -> int COMMA elementosInternosInt','elementosInternosInt',3,'p_elementosInternosInt','scalaSintactico.py',48),
  ('elementosInternosDouble -> double','elementosInternosDouble',1,'p_elementosInternosDouble','scalaSintactico.py',51),
  ('elementosInternosDouble -> double COMMA elementosInternosDouble','elementosInternosDouble',3,'p_elementosInternosDouble','scalaSintactico.py',52),
  ('elementosInternosBool -> booleano','elementosInternosBool',1,'p_elementosInternosBool','scalaSintactico.py',55),
  ('elementosInternosBool -> booleano COMMA elementosInternosBool','elementosInternosBool',3,'p_elementosInternosBool','scalaSintactico.py',56),
  ('elementosInternosString -> string','elementosInternosString',1,'p_elementosInternosString','scalaSintactico.py',59),
  ('elementosInternosString -> string COMMA elementosInternosString','elementosInternosString',3,'p_elementosInternosString','scalaSintactico.py',60),
  ('elementosInternos2 -> int','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',63),
  ('elementosInternos2 -> double','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',64),
  ('elementosInternos2 -> booleano','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',65),
  ('elementosInternos2 -> string','elementosInternos2',1,'p_elementosInternos2','scalaSintactico.py',66),
  ('elementosInternos2 -> int COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',67),
  ('elementosInternos2 -> double COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',68),
  ('elementosInternos2 -> booleano COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',69),
  ('elementosInternos2 -> string COMMA elementosInternos2','elementosInternos2',3,'p_elementosInternos2','scalaSintactico.py',70),
  ('valueCons -> string','valueCons',1,'p_valueCons','scalaSintactico.py',73),
  ('valueCons -> booleano','valueCons',1,'p_valueCons','scalaSintactico.py',74),
  ('valueCons -> tupla','valueCons',1,'p_valueCons','scalaSintactico.py',75),
  ('tipo -> INT','tipo',1,'p_tipo','scalaSintactico.py',78),
  ('tipo -> DOUBLE','tipo',1,'p_tipo','scalaSintactico.py',79),
  ('tipo -> BOOL','tipo',1,'p_tipo','scalaSintactico.py',80),
  ('tipo -> STRING_TYPE','tipo',1,'p_tipo','scalaSintactico.py',81),
  ('tipoValue -> STRING_TYPE EQUAL string','tipoValue',3,'p_tipoValue','scalaSintactico.py',85),
  ('tipoValue -> BOOL EQUAL booleano','tipoValue',3,'p_tipoValue','scalaSintactico.py',86),
  ('tipoValue -> INT EQUAL int','tipoValue',3,'p_tipoValue','scalaSintactico.py',87),
  ('tipoValue -> DOUBLE EQUAL double','tipoValue',3,'p_tipoValue','scalaSintactico.py',88),
  ('tipoValue -> ARRAY LBRACK INT RBRACK EQUAL NEW ARRAY LBRACK INT RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',89),
  ('tipoValue -> ARRAY LBRACK DOUBLE RBRACK EQUAL NEW ARRAY LBRACK DOUBLE RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',90),
  ('tipoValue -> ARRAY LBRACK BOOL RBRACK EQUAL NEW ARRAY LBRACK BOOL RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',91),
  ('tipoValue -> ARRAY LBRACK STRING_TYPE RBRACK EQUAL NEW ARRAY LBRACK STRING_TYPE RBRACK LPAREN int RPAREN','tipoValue',13,'p_tipoValue','scalaSintactico.py',92),
  ('tipoValue -> LIST LBRACK INT RBRACK EQUAL LIST LPAREN elementosInternos RPAREN','tipoValue',9,'p_tipoValue','scalaSintactico.py',93),
  ('tipoValue -> LIST LBRACK DOUBLE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN','tipoValue',9,'p_tipoValue','scalaSintactico.py',94),
  ('tipoValue -> LIST LBRACK BOOL RBRACK EQUAL LIST LPAREN elementosInternos RPAREN','tipoValue',9,'p_tipoValue','scalaSintactico.py',95),
  ('tipoValue -> LIST LBRACK STRING_TYPE RBRACK EQUAL LIST LPAREN elementosInternos RPAREN','tipoValue',9,'p_tipoValue','scalaSintactico.py',96),
  ('tipoValueCons -> STRING_TYPE EQUAL string','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',99),
  ('tipoValueCons -> BOOL EQUAL booleano','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',100),
  ('tipoValueCons -> INT EQUAL int','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',101),
  ('tipoValueCons -> DOUBLE EQUAL double','tipoValueCons',3,'p_tipoValueCons','scalaSintactico.py',102),
  ('tupla -> LPAREN elementosInternos2 RPAREN','tupla',3,'p_tupla','scalaSintactico.py',105),
  ('funcionesTupla -> tuplaSwap','funcionesTupla',1,'p_funcionesTupla','scalaSintactico.py',108),
  ('funcionesTupla -> tuplaToString','funcionesTupla',1,'p_funcionesTupla','scalaSintactico.py',109),
  ('funcionesTupla -> tuplaProductIterator','funcionesTupla',1,'p_funcionesTupla','scalaSintactico.py',110),
  ('tuplaSwap -> ID DOT SWAP','tuplaSwap',3,'p_tuplaSwap','scalaSintactico.py',113),
  ('tuplaToString -> ID DOT TOSTRING LPAREN RPAREN','tuplaToString',5,'p_tuplaToString','scalaSintactico.py',116),
  ('tuplaProductIterator -> ID DOT PRODUCTITERATOR','tuplaProductIterator',3,'p_tuplaProductIterator','scalaSintactico.py',119),
  ('funcionesArray -> arrayHead','funcionesArray',1,'p_funcionesArray','scalaSintactico.py',122),
  ('funcionesArray -> arrayTail','funcionesArray',1,'p_funcionesArray','scalaSintactico.py',123),
  ('funcionesArray -> arrayLength','funcionesArray',1,'p_funcionesArray','scalaSintactico.py',124),
  ('funcionesPropias -> INPUT LPAREN RPAREN','funcionesPropias',3,'p_funcionesPropias','scalaSintactico.py',127),
  ('funcionesPropias -> PRINTLN LPAREN string RPAREN','funcionesPropias',4,'p_funcionesPropias','scalaSintactico.py',128),
  ('funcionesPropias -> PRINTLN LPAREN booleano RPAREN','funcionesPropias',4,'p_funcionesPropias','scalaSintactico.py',129),
  ('funcionesPropias -> PRINTLN LPAREN ID RPAREN','funcionesPropias',4,'p_funcionesPropias','scalaSintactico.py',130),
  ('funcionesPropias -> PRINTLN LPAREN expression RPAREN','funcionesPropias',4,'p_funcionesPropias','scalaSintactico.py',131),
  ('arrayHead -> ID DOT HEAD','arrayHead',3,'p_arrayHead','scalaSintactico.py',134),
  ('arrayTail -> ID DOT TAIL','arrayTail',3,'p_arrayTail','scalaSintactico.py',137),
  ('arrayLength -> ID DOT LENGTH','arrayLength',3,'p_arrayLength','scalaSintactico.py',140),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','scalaSintactico.py',143),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','scalaSintactico.py',147),
  ('expression -> term','expression',1,'p_expression_term','scalaSintactico.py',151),
  ('term -> term TIMES factor','term',3,'p_term_times','scalaSintactico.py',155),
  ('term -> term DIVIDE factor','term',3,'p_term_div','scalaSintactico.py',159),
  ('term -> factor','term',1,'p_term_factor','scalaSintactico.py',163),
  ('sentencia -> IF factor comparacion factor LBRACE cuerpo RBRACE','sentencia',7,'p_sentencia_if','scalaSintactico.py',167),
  ('for -> FOR LPAREN ID LM ID RPAREN LBRACE cuerpo RBRACE','for',9,'p_for','scalaSintactico.py',171),
  ('comparacionesVar -> ID DOT EQUALS LPAREN ID RPAREN','comparacionesVar',6,'p_comparacionesVar','scalaSintactico.py',175),
  ('comparacionesVar -> ID DOT EQ LPAREN ID RPAREN','comparacionesVar',6,'p_comparacionesVar','scalaSintactico.py',176),
  ('comparacion -> GT','comparacion',1,'p_comparacion','scalaSintactico.py',179),
  ('comparacion -> GE','comparacion',1,'p_comparacion','scalaSintactico.py',180),
  ('comparacion -> LT','comparacion',1,'p_comparacion','scalaSintactico.py',181),
  ('comparacion -> LE','comparacion',1,'p_comparacion','scalaSintactico.py',182),
  ('comparacion -> EQUAL2','comparacion',1,'p_comparacion','scalaSintactico.py',183),
  ('factor -> int','factor',1,'p_factor_int','scalaSintactico.py',186),
  ('factor -> double','factor',1,'p_factor_double','scalaSintactico.py',189),
  ('booleano -> TRUE','booleano',1,'p_booleano','scalaSintactico.py',192),
  ('booleano -> FALSE','booleano',1,'p_booleano','scalaSintactico.py',193),
  ('string -> STRING','string',1,'p_string','scalaSintactico.py',196),
  ('double -> DOUBLE_NUMBER','double',1,'p_double','scalaSintactico.py',199),
  ('int -> INT_NUMBER','int',1,'p_int','scalaSintactico.py',202),
]
