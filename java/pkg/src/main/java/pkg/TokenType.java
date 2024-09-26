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
    MINUS("-"),
    BANG("!"),
    ASTERISK("*"),
    SLASH("/"),
    LESSTHAN("<"),
    GREATERTHAN(">"),

    //Delimiters
    COMMA(","),
    SEMICOLON(";"),

    LPAREN("("),
    RPAREN(")"),
    LBRACE("{"),
    RBRACE("}"),

    //Keywords
    FUNCTION("FUNCTION"),
    LET("LET"),
    TRUE("TRUE"),
    FALSE("FALSE"),
    IF("IF"),
    ELSE("ELSE"),
    RETURN("RETURN"),
    EQUALS("=="),
    NOT_EQUALS("!=");
    





    // Literal meaning of the token
    private final String literal;

    TokenType(String literal){
      this.literal = literal;
    }


    public String getLiteral() {
      return literal;
    }

}

