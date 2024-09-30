package pkg.ast.statements;
import pkg.ast.Node;
import pkg.Token;


// Statement class used for all statements
public abstract class Statement extends Node{

  // Statement constructor
  public Statement(Token token){
    super(token);
  }

}

