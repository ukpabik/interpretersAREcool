// Lexer for Swift Language

import Foundation
// Tokens ENUM
public enum TokenType: String {

    case ILLEGAL = "ILLEGAL"
    case EOF = "EOF"
    case IDENT = "IDENT"
    case INT = "INT"
    case ASSIGN = "="
    case PLUS = "+"
    case COMMA = ","
    case SEMICOLON = ";"
    case LPAREN = "("
    case RPAREN = ")"
    case LBRACE = "{"
    case RBRACE = "}"
    case FUNCTION = "FUNCTION"
    case LET = "LET"

        // Keywords
    case TRUE = "TRUE"
    case FALSE = "FALSE"
    case IF = "IF"
    case ELSE = "ELSE"
    case RETURN = "RETURN"
    case EQ = "=="
    case NOT_EQ = "!="
    case BANG = "!"

}

// Create Token object
public struct Token {
    let type: TokenType
        let literal: String
}

// Create object for Lexer
public struct Lexer {
    let input: String
        var position: String.Index
        var readPosition: String.Index
        var ch: Character?

        // Initialize Lexer
        init(input: String){
            self.input = input
                self.position = input.startIndex
                self.readPosition = input.startIndex
                self.ch = nil
                readChar()
        }

    // Use mutating keyword because the value could change
    // Reads the next char 
    mutating func readChar() -> Void {
        if readPosition < input.endIndex{
            ch = input[readPosition]
                // Update the index
                readPosition = input.index(after: readPosition)
        }
        else{
            ch = nil
        }
    }

    // Peek at the next char: This function could return a char or nil
    mutating func peekChar() -> Character?{
        if readPosition < input.endIndex{
            return input[readPosition]
        }
        else{
            return nil
        }
    }

    // Gets the value of the next token and returns it
    mutating func nextToken() -> Token {

        skipWhitespace()

            let tok: Token

            switch ch{
                case "=":
                    if peekChar() == "="{
                        let position = readPosition
                            readChar()
                            let literal = String(input[position..<readPosition])
                            tok = Token(type: .EQ, literal: literal)
                    } 
                    else{
                        tok = Token(type: .ASSIGN, literal: String(ch!))
                    }
                case "!":
                    if peekChar() == "="{
                        let position = readPosition
                            readChar()
                            let literal = String(input[position..<readPosition])
                            tok = Token(type: .NOT_EQ, literal: literal)
                    } 
                    else{
                        tok = Token(type: .BANG, literal: String(ch!))
                    }
                case "+":
                    tok = Token(type: .PLUS, literal: String(ch!))
                case ",":
                        tok = Token(type: .COMMA, literal: String(ch!))
                case ";":
                            tok = Token(type: .SEMICOLON, literal: String(ch!))
                case "(":
                                tok = Token(type: .LPAREN, literal: String(ch!))
                case ")":
                                    tok = Token(type: .RPAREN, literal: String(ch!))
                case "{":
                                        tok = Token(type: .LBRACE, literal: String(ch!))
                case "}":
                                            tok = Token(type: .RBRACE, literal: String(ch!))
                case let c? where isLetter(c):
                                                let literal = readIdentifier()

                                                    let type: TokenType = lookupIdent(literal)

                                                    return Token(type: type, literal: literal)
                case let c? where isDigit(c):
                                                    let literal = readNumber()

                                                        return Token(type: .INT, literal: literal)
                case nil:
                                                        tok = Token(type: .EOF, literal: "")
                default:
                                                            tok = Token(type: TokenType.ILLEGAL, literal: String(ch!))

            }
        readChar()
            return tok
    }

    // Check to see if the char is whitespace
    func isWhitespace(_ c: Character) -> Bool{
        return c == " " || c == "\t" || c == "\r" || c == "\n"
    }

    // Skip the whitespace
    mutating func skipWhitespace(){
        while let current = ch, current.isWhitespace{
            readChar()
        }
    }

    // Checks if the char is a letter
    // Use an underscore in the params, to not have to have a label
    // when calling the function
    func isLetter(_ c: Character) -> Bool{
        return c >= "a" && c <= "z" || c >= "A" && c <= "Z" || c == "_"
    }

    // Checks if the char is a digit
    func isDigit(_ c: Character) -> Bool{
        return c >= "0" && c <= "9"
    }

    // Lookup the identifier
    func lookupIdent(_ ident: String) -> TokenType{
        switch ident{
            case "fn":
                return .FUNCTION
            case "let":
                    return .LET
            case "if":
                        return .IF
            case "else":
                            return .ELSE
            case "return":
                                return .RETURN
            case "true":
                                    return .TRUE
            case "false":
                                        return .FALSE
            default:
                                            return .IDENT
        }
    }

    // Read Identifier
    mutating func readIdentifier() -> String{
        var position = position
            while isLetter(ch!){
                readChar()
            }
        return String(input[position..<readPosition])
    }

    // Read Number
    mutating func readNumber() -> String{
        var position = position
            while isDigit(ch!){
                readChar()
            }
        return String(input[position..<readPosition])
    }


    func testNextToken() {
        let input = """
            let five = 5;
        let ten = 10;

        let add = fn(x, y) {
            x + y;
        };

        let result = add(five, ten);

        if (result == 15) {
            return true;
        } else {
            return false;
        }

        """

            var lexer = Lexer(input: input)
            var tok = lexer.nextToken()
            while tok.type != .EOF {
                print(tok)
                    tok = lexer.nextToken()
            }

    }
}
