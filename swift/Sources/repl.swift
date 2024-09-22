// REPL (Read, Eval, Print, Loop)

import Foundation

func repl() {
    print("REPL. Type 'exit' to quit.")
    
    while true {
        // Prompt the user
        print(">> ", terminator: "")
        
        // Read user input
        guard let input = readLine() else {
            print("Error reading input. Exiting REPL.")
            break
        }
        
        // Exit condition
        if input.lowercased() == "exit" {
            print("Goodbye!")
            break
        }
        
        // Initialize Lexer with user input
        var lexer = Lexer(input: input)
        
        // Tokenize input and print tokens
        var tok = lexer.nextToken()
        while tok.type != .EOF {
            print(tok)
            tok = lexer.nextToken()
        }
    }
}
