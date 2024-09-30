package pkg.ast.statements;


// Class for let statement
public class LetStatement extends Statement{

  // LetStatement fields
  private Token token;
  private IdentifierExpression name;
  private Expression value;


  // Function for statement node
  public void statementNode(){
  }

  // Function for getting the token literal
  public String getTokenLiteral(){
    return this.token.getLiteral();
  }
}
