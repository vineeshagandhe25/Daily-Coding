// Java program to evaluate a postfix expression

import java.util.Stack;

public class PostfixExpression {

    public static int evaluatePostfix(String expression) {
        // Create a stack to store operands
        Stack<Integer> stack = new Stack<>();

        // Traverse the expression
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);

            // If the character is a digit, push it to the stack
            if (Character.isDigit(c)) {
                stack.push(c - '0');
            }
            
            // Otherwise, the character is an operator
            else {
                // Pop two operands from stack
                int operand2 = stack.pop();
                int operand1 = stack.pop();

                // Apply the operator and push the result back to the stack
                switch (c) {
                    case '+':
                        stack.push(operand1 + operand2);
                        break;
                    case '-':
                        stack.push(operand1 - operand2);
                        break;
                    case '*':
                        stack.push(operand1 * operand2);
                        break;
                    case '/':
                        stack.push(operand1 / operand2);
                        break;
                }
            }
        }

        // The final result will be in the top of the stack
        return stack.pop();
    }

    public static void main(String[] args) {
        String expression = "231*+9-";
        System.out.println("Postfix Expression: " + expression);
        System.out.println("Evaluation Result: " + evaluatePostfix(expression));
    }
    
}

// Time Complexity --- O(n) where n is length of given expression.
// Space Complexity --- O(n) where n is length of given expression.