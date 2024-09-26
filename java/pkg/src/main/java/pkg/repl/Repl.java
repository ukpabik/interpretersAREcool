package pkg.repl;

import pkg.lexer.Lexer;
import pkg.Token;
import pkg.TokenType;

import java.util.Scanner;


// Stands for Read, Eval, Print, Loop
public class Repl {

  // Initial prompt
  String prompt = ">> ";

  // Start function that starts the repl
  public void start(Scanner s){

    while (true){
      System.out.print(prompt);
      String input = s.nextLine();
      if (input == null || input.equals("exit")){
        break;
      }

      // Initialize a lexer with the input from the user
      Lexer lexer = new Lexer(input);
      // Read through the tokens in the input
      while (true){
        Token token = lexer.nextToken();
        if (token.getType() == TokenType.EOF){
          break;
        }
        System.out.println(token.getLiteral());
      }

    }

  }

}
