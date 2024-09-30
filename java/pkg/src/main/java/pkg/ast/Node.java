package pkg.ast;

import pkg.Token;

// The node class for the abstract syntax tree
public abstract class Node {

  // The token associated with this node
  private final Token token;

  // The constructor for the Node class
  public Node(Token t){
    this.token = t;
  }

  // Getter for the token
  public Token getToken(){
    return token;
  }

  // Getter for the token literal value
  public String getTokenLiteral(){
    return token.getLiteral();
  }

}
