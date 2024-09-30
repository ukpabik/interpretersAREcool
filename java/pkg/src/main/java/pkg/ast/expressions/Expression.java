package pkg.ast.expressions;

import pkg.ast.Node;
import pkg.Token;

// Expression class used for all expressions
public abstract class Expression extends Node {

  // Expression constructor
  public Expression(Token token){
    super(token);
  }
}
