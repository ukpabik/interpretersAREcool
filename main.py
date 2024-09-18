# main.py

from lexer import Lexer
from parser import parser
from interpreter import evaluate
from environment import Environment

def main():
    env = Environment()
    print("Welcome to the Calc Interpreter!")
    print("Type 'exit' or 'quit' to exit.\n")

    while True:
        try:
            s = input('calc > ')
            if s.strip().lower() in ('exit', 'quit'):
                print("Goodbye!")
                break
            if not s:
                continue  # Skip empty input

            # Parse the input
            ast = parser.parse(s, lexer=lexer_instance.lexer)

            # Evaluate each statement in the AST
            for stmt in ast:
                result = evaluate(stmt, env)
                if result is not None:
                    print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    # Initialize and build the lexer
    lexer_instance = Lexer()
    lexer_instance.build()
    main()

