package src;

  enum TokenType{
    ILLEGAL("ILLEGAL"),
    EOF("EOF"),

    //Identifiers + literals
    IDENT("IDENT"),
    INT("INT"),

    //Operators
    ASSIGN("ASSIGN"),
    PLUS("PLUS"),

    //Delimiters
    COMMA(","),
    SEMICOLON(";"),

    LPAREN("("),
    RPAREN(")"),
    LBRACE("{"),
    RBRACE("}"),

    //Keywords
    FUNCTION("FUNCTION"),
    LET("LET");
    





    // Literal meaning of the token
    private final String literal;

    TokenType(String literal){
      this.literal = literal;
    }


    public String getLiteral() {
      return literal;
    }
}


public class Token{
  
  private TokenType type;
  private String literal;



  public Token(TokenType newType){
    this.type = newType;
    this.literal = newType.getLiteral();
  }
}
