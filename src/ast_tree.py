
class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Number({self.value})'

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'BinOp({self.left}, "{self.op}", {self.right})'

class Assign:
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

    def __repr__(self):
        return f'Assign("{self.id}", {self.expression})'

class If:
    def __init__(self, condition, body, orelse=None):
        self.condition = condition
        self.body = body
        self.orelse = orelse
    def __repr__(self):
        if self.orelse:
            return f'If({self.condition}, {self.body}, Else({self.orelse}))'
        return f'If({self.condition}, {self.body})'

class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f'While({self.condition}, {self.body})'

class For:
    def __init__(self, expression1, condition, expression2, body):
        self.expression1 = expression1
        self.condition = condition
        self.expression2 = expression2
        self.body = body

    def __repr__(self):
        return f'For({self.expression1}, {self.condition}, {self.expression2}, {self.body})'

class FuncDef:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return f'FuncDef(name={self.name}, params={self.params}, body={self.body})'

class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f'FunctionCall(name={self.name}, args={self.args})'

class Return:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f'Return(expr={self.expr})'
