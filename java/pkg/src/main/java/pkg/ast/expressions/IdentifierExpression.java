package pkg.ast.expressions;

import pkg.Token;


// IdentifierExpression class used for identifier expressions
public class IdentifierExpression extends Expression {

  private Token identifier;
  private String value;

  // IdentifierExpression constructor
  public IdentifierExpression(Token t, String v){
    super(t);
    this.identifier = t;
    this.value = v;
  }

  public void expressionNode(){
  }

  // Function for getting the token literal
  public String getTokenLiteral(){
    return this.identifier.getLiteral();
  }
}
