from ast_tree import Number, BinOp, Assign, If
from environment import Environment

def evaluate(node, env):
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, BinOp):
        left = evaluate(node.left, env)
        right = evaluate(node.right, env)

        op = node.op

        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        elif op == '*':
            return left * right
        elif op == '>':
            return left > right
        elif op == '<':
            return left < right
        else:
            raise Exception(f"Unknown operator {op}")

    elif isinstance(node, Assign):
        value = evaluate(node.expression, env)
        env.variables[node.id] = value
        return value

    elif isinstance(node, If):
        condition = evaluate(node.condition, env)
        if condition:
            for statement in node.body:
                evaluate(statement, env)
        return None
    elif isinstance(node, str):
        if node in env.variables:
            return env.variables[node]
        else:
            raise Exception(f"Undefined variable {node}")

    else:
        raise Exception(f"Unknown node type: {type(node)}")

