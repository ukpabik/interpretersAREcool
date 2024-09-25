package pkg.lexer;

import pkg.Token;
import pkg.TokenType;


public class Lexer {

  // Lexer fields
  private String input;
  private int position;
  private int readPosition;
  private char ch;


  // Initializes the lexer
  public Lexer(String input) {
    this.input = input;
    this.position = 0;
    this.readPosition = 0;
    this.ch = input.charAt(0);
    this.readChar();
  }

  // Helper method that gives us the next char and advances position in the input
  public void readChar(){
    // Check if we reach the end of the input
    if (this.readPosition >= this.input.length()){
      // Sets the char to 0 (EOF)
      this.ch = 0;
    }
    else{
      this.ch = this.input.charAt(this.readPosition);
    }
    this.position = this.readPosition;
    this.readPosition += 1;
  }


  // Reads the next token
  public Token nextToken(){
    Token tok = new Token();

    this.skipWhitespace();

    switch(this.ch){
      case '=':
        tok = new Token(TokenType.ASSIGN);
        break;
      case ';':
        tok = new Token(TokenType.SEMICOLON);
        break;
      case '(':
        tok = new Token(TokenType.LPAREN);
        break;
      case ')':
        tok = new Token(TokenType.RPAREN);
        break;
      case ',':
        tok = new Token(TokenType.COMMA);
        break;
      case '+':
        tok = new Token(TokenType.PLUS);
        break;
      case '{':
        tok = new Token(TokenType.LBRACE);
        break;
      case '}':
        tok = new Token(TokenType.RBRACE);
        break;

      case 0:
        tok.setLiteral("");
        tok.setType(TokenType.EOF);
        break;

      default:
        if (isLetter(this.ch)){
          tok.setLiteral(this.readIdentifier());
          tok.setType(TokenType.IDENT);
          return tok;

        }
        else if (isDigit(this.ch)){
          tok.setType(TokenType.INT);
          tok.setLiteral(this.readNumber());
          return tok;
        }
        else{
          tok = new Token(TokenType.ILLEGAL);
          return tok;
        }

    }

    this.readChar();
    return tok;

  }

  // Function that skips whitespace
  public void skipWhitespace(){
    while (this.ch == ' ' || this.ch == '\t' || this.ch == '\n' || this.ch == '\r'){
      this.readChar();
    }
  }

  // Function that reads an identifier
  public String readIdentifier(){
    int position = this.position;
    while (isLetter(this.ch)){
      this.readChar();
    }
    return this.input.substring(position, this.position);

  }


  // Function that reads a number
  public String readNumber(){
    int pos = this.position;
    while (isDigit(this.ch)){
      this.readChar();
    }
    return this.input.substring(pos, this.position);
  }


  // Checks if the given char is a digit
  public boolean isDigit(char ch){
    return '0' <= ch && ch <= '9';
  }

  // Checks if the given char is a letter
  public boolean isLetter(char ch){
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || ch == '_';
  }

  // Generates a new token with the given tokentype
  public Token newToken(TokenType newType){
    return new Token(newType);
  }

}
