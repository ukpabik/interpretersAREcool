package pkg.ast;

import pkg.Token;

public abstract class Node {

  private final Token token;

  public Node(Token t){
    this.token = t;
  }

  public Token getToken(){
    return token;
  }

  public String getTokenLiteral(){
    return token.getLiteral();
  }

}
