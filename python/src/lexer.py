import ply.lex as lex
# Tokenizer for a simple expression evaluator for numbers and operators

class Lexer(object):


    # Reserved key words
    reserved = {
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            }


    # List of token names
    tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'LBRACE',
        'RBRACE',
        'ID',
        'ASSIGN',
        'SEMICOLON',
        'GREATERTHAN',
        'LESSTHAN',
        
        ] + list(reserved.values())

    # Expression rules for simple tokens, special prefix 't_' to indicate it is a token
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_ASSIGN = r'='
    t_SEMICOLON = r';'
    t_GREATERTHAN = r'>'
    t_LESSTHAN = r'<'

    # A regular expression

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Tracking new lines | Line number increased by input value
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Checking for reserved words
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    # Ignored characters i.e. tabs and spaces
    t_ignore = ' \t'

    # Error handling
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Discard any tokens that are comments
    def t_COMMENT(self, t):
        r'\#.*'
        pass

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    
    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token)
    


# Iterating through lexer tokens
# They come out as this: Type, Value, Line #, Lex Position
m = Lexer()
m.build()
m.test('if (a > 0) { a = 1; } else { a = 0; }')
# To use lexer, feed it input text using input(), and then
# after, repeated calls to token() produces the tokens.




