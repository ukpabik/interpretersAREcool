
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programleftPLUSMINUSleftTIMESDIVIDErightUMINUSASSIGN DIVIDE ELSE GREATERTHAN ID IF LBRACE LESSTHAN LPAREN MINUS NUMBER PLUS RBRACE RPAREN SEMICOLON THEN TIMESprogram : program statementprogram : statementstatement : ID ASSIGN expression PLUSexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression GREATERTHAN expression\n                  | expression LESSTHAN expressionexpression : MINUS expression %prec UMINUSexpression : NUMBERexpression : IDstatement : IF LPAREN expression RPAREN LBRACE statements RBRACEstatements : statements statementstatements : statement'
    
_lr_action_items = {'ID':([0,1,2,5,6,7,10,13,14,15,16,17,18,21,28,29,30,31,32,],[3,3,-2,-1,8,8,8,-3,8,8,8,8,8,8,3,3,-15,-13,-14,]),'IF':([0,1,2,5,13,28,29,30,31,32,],[4,4,-2,-1,-3,4,4,-15,-13,-14,]),'$end':([1,2,5,13,31,],[0,-2,-1,-3,-13,]),'ASSIGN':([3,],[6,]),'LPAREN':([4,],[7,]),'MINUS':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,],[10,10,-12,14,10,-11,14,10,10,10,10,10,10,-10,10,-4,-5,-6,-7,14,14,]),'NUMBER':([6,7,10,13,14,15,16,17,18,21,],[11,11,11,11,11,11,11,11,11,11,]),'PLUS':([8,9,11,12,19,22,23,24,25,26,27,],[-12,13,-11,21,-10,-4,-5,-6,-7,21,21,]),'TIMES':([8,9,11,12,19,22,23,24,25,26,27,],[-12,15,-11,15,-10,15,15,-6,-7,15,15,]),'DIVIDE':([8,9,11,12,19,22,23,24,25,26,27,],[-12,16,-11,16,-10,16,16,-6,-7,16,16,]),'GREATERTHAN':([8,9,11,12,19,22,23,24,25,26,27,],[-12,17,-11,17,-10,-4,-5,-6,-7,17,17,]),'LESSTHAN':([8,9,11,12,19,22,23,24,25,26,27,],[-12,18,-11,18,-10,-4,-5,-6,-7,18,18,]),'RPAREN':([8,11,12,19,22,23,24,25,26,27,],[-12,-11,20,-10,-4,-5,-6,-7,-8,-9,]),'RBRACE':([13,29,30,31,32,],[-3,31,-15,-13,-14,]),'LBRACE':([20,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,28,29,],[2,5,30,32,]),'expression':([6,7,10,13,14,15,16,17,18,21,],[9,12,19,22,23,24,25,26,27,22,]),'statements':([28,],[29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program_multiple','parser.py',16),
  ('program -> statement','program',1,'p_program_single','parser.py',20),
  ('statement -> ID ASSIGN expression PLUS','statement',4,'p_statement_assign','parser.py',24),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',28),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',29),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',30),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',31),
  ('expression -> expression GREATERTHAN expression','expression',3,'p_expression_binop','parser.py',32),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_binop','parser.py',33),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',43),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',47),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',51),
  ('statement -> IF LPAREN expression RPAREN LBRACE statements RBRACE','statement',7,'p_statement_if','parser.py',55),
  ('statements -> statements statement','statements',2,'p_statements_multiple','parser.py',59),
  ('statements -> statement','statements',1,'p_statements_single','parser.py',63),
]