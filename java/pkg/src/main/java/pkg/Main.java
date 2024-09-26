package pkg;

import java.util.Scanner;
import pkg.repl.Repl;


// Main class for testing the repl

public class Main {
  public static void main(String[] args){
    System.out.println("Hello. This is the Java REPL.");
    System.out.println("Type \"exit\" to exit.");
    Scanner s = new Scanner(System.in);
    Repl repl = new Repl();
    repl.start(s);
  }

}
