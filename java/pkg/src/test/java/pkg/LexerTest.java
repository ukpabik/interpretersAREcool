package pkg;

import pkg.lexer.Lexer;
import pkg.Token;
import pkg.TokenType;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;
import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;



public class LexerTest {


  // Test function for testing base input
  @Test
    public void testLexerTokens() {
        // Test entire valid string input
        String input = "let five = 5; let ten = 10; let add = fn(x, y) { x + y; }; let result = add(five, ten); !-/*5; 5 < 10 > 5;  if (5 < 10) { return true; } else { return false; }  10 == 10; 10 != 9;";
        
        // Create a new lexer
        Lexer lexer = new Lexer(input);

        // List of the expected values
        List<String> expected = Arrays.asList(
            "let",
            "five",
            "=",
            "5",
            ";",
            "let",
            "ten",
            "=",
            "10",
            ";",
            "let",
            "add",
            "=",
            "fn",
            "(",
            "x",
            ",",
            "y",
            ")",
            "{",
            "x",
            "+",
            "y",
            ";",
            "}",
            ";",
            "let",
            "result",
            "=",
            "add",
            "(",
            "five",
            ",",
            "ten",
            ")",
            ";",
            "!",
            "-",
            "/",
            "*",
            "5",
            ";",
            "5",
            "<",
            "10",
            ">",
            "5",
            ";",
            "if",
            "(",
            "5",
            "<",
            "10",
            ")",
            "{",
            "return",
            "true",
            ";",
            "}",
            "else",
            "{",
            "return",
            "false",
            ";",
            "}",
            "10",
            "==",
            "10",
            ";",
            "10",
            "!=",
            "9",
            ";"
        );

        // Loop through all of the expected tokens
        int i = 0;
        while (true) {
            Token token = lexer.nextToken();

            String actual = token.getLiteral();
            System.out.println(actual);

            // assert that the actual token matches the expected
            assertEquals(expected.get(i), actual, "Token at index " + i + " does not match.");

            // check if we have reached the end of the input
            if (actual.equals("EOF") || i == expected.size() - 1) {
                break;
            }
            i++;
        }

        // assert that all expected tokens were consumed
        assertEquals(expected.size() - 1, i, "Not all expected tokens were matched.");
    }
}

