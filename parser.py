#  parser.py
import ply.yacc as yacc
from lexer import Lexer
from ast_tree import Number, BinOp, Assign, If
from interpreter import evaluate
from environment import Environment

lexer_instance = Lexer()
lexer_instance.build()

tokens = lexer_instance.tokens

# Parsing rules

def p_program_multiple(p):
    'program : program statement'
    p[0] = p[1] + [p[2]]

def p_program_single(p):
    'program : statement'
    p[0] = [p[1]]

def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    p[0] = Assign(p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GREATERTHAN expression
                  | expression LESSTHAN expression'''
    p[0] = BinOp(p[1], p[2], p[3])

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Number(p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]  # Will handle in evaluation

def p_statement_if(p):
    'statement : IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'
    p[0] = If(p[3], p[6], p[10])

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]



def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

start = 'program'

# Build the parser
parser = yacc.yacc()

# Test it
if __name__ == '__main__':
    data = 'if (a > 0) { a = 1; }'
    env = Environment()
    result = parser.parse(data, lexer = lexer_instance.lexer)
    for statement in result:
        evaluate(statement, env)
    print(env.variables)

