package pkg.parser;

// Java class for the parser

// Builds the AST data structure (abstract syntax tree)


// This parser will use the recursive descent structure
// Otherwise known as a "Pratt parser"


import pkg.ast.*;
import pkg.lexer.*;
import pkg.Token;
import pkg.TokenType;


public class Parser {
  // Parser fields
  private Lexer lexer;
  private Token currentToken;
  private Token peekToken;
  
  public Parser(Lexer l){
    this.lexer = l;
    this.currentToken = this.lexer.nextToken();
    this.peekToken = this.lexer.nextToken();
  }

  // Function that gets the next token by moving the tokens forward
  public void nextToken(){
    this.currentToken = this.peekToken;
    this.peekToken = this.lexer.nextToken();
  }

  public Program parseProgram(){
    return null;
  }
}
