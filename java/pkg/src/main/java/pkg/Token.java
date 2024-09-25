package pkg;

import pkg.TokenType;
import java.util.Map;
import java.util.HashMap;

public class Token {
  
  // Token fields
  private TokenType type;
  private String literal;

  // Map of all keywords
  Map<String, String> keywords = new HashMap<String, String>(

      Map.of("fn", "FUNCTION",
          "let", "LET"
  )); 


  // Initializes a blank token
  public Token() {
    this.type = null;
    this.literal = "";
  }


  // Initializes a new token with the given tokentype
  public Token(TokenType newType){
    this.type = newType;
    this.literal = newType.getLiteral();
  }


  // Returns the literal
  public String getLiteral() {
    return literal;
  }


  // Sets the literal
  public void setLiteral(String literal) {
    this.literal = literal;
  }


  // Returns the type
  public TokenType getType() {
    return type;
  }

  // Sets the type
  public void setType(TokenType type) {
    this.type = type;
  }

  // Returns the type of the given identifier
  public TokenType lookUpIdent(String ident){
    if (ident.equals("fn")){
      return TokenType.FUNCTION;
    }
    else if (ident.equals("let")){
      return TokenType.LET;
    }
    else{
      return TokenType.IDENT;
    }
  }
}
