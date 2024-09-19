
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
