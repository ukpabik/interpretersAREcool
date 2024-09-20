from ast_tree import Number, BinOp, Assign, If, While, For
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
        else:
            if node.orelse:
                for statement in node.orelse:
                    evaluate(statement, env)
        return None

    elif isinstance(node, While):
        condition = evaluate(node.condition, env)
        if condition:
            while True:
                if not condition:
                    break
                for statement in node.body:
                    evaluate(statement, env)
                condition = evaluate(node.condition, env)
                print(condition)
        return None

    elif isinstance(node, For):
        value = evaluate(node.expression1, env)
        print(value)
        while True:
            condition = evaluate(node.condition, env)
            if not condition:
                break
            for statement in node.body:

                evaluate(statement, env) 
            index = evaluate(node.expression2, env)
            print(index) 
        return None

    elif isinstance(node, str):
        if node in env.variables:
            return env.variables[node]
        else:
            raise Exception(f"Undefined variable {node}")

    else:
        raise Exception(f"Unknown node type: {type(node)}")

