package pkg.ast;


import pkg.ast.statements.Statement;
import java.util.ArrayList;
import java.util.List;


// Program class used for the entire program
// Root node for every AST the parser produces
public class Program extends Node{
  private final List<Statement> statements = new ArrayList<>();


  // Program constructor
  public Program(){
    super(null);
  }

  public List<Statement> getStatements(){
    return this.statements;
  }

  // Function for getting the token literal of the first statement
  @Override
  public String getTokenLiteral(){
    if (statements.size() > 0){
      return this.statements.get(0).getTokenLiteral();
    }
    else{
      return "";
    }
  }
}
