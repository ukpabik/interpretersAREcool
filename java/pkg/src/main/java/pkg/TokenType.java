package pkg;

public enum TokenType{

    ILLEGAL("ILLEGAL"),
    EOF("EOF"),

    //Identifiers + literals
    IDENT("IDENT"),
    INT("INT"),

    //Operators
    ASSIGN("="),
    PLUS("+"),

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

