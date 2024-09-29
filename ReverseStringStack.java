/*Reverse a string using stack  */

import java.util.Stack;

class ReverseStringStack {

    public static void main(String[] args) {

        String original = "Hello, World!";
        String reversed = reverseString(original);
        System.out.println("Original String: " + original);
        System.out.println("Reversed String: " + reversed);

    }

    public static String reverseString(String input) {

        Stack<Character> stack = new Stack<>();

        for (char ch : input.toCharArray()) {
            stack.push(ch);
        }

        // Pop characters from the stack and append to result
        StringBuilder reversed = new StringBuilder();

        while (!stack.isEmpty()) {
            reversed.append(stack.pop());
        }

        return reversed.toString();
    }
}

// Time Complexity --- O(n) where n is length of given input string .
// Space Complexity --- O(n) where n is length of given input string .