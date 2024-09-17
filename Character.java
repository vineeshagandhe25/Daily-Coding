// Wrtie a program to give the following output for the given input
/*Input :a1b10
 * Output : abbbbbbbbbb
 */
class CharacterDemo {
    public static void main(String[] args) {
        String input = "a1b10";
        printChars(input);
    }

    public static void printChars(String str) {
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (Character.isLetter(ch)) {
                System.out.print(ch);
            }

            else if (Character.isDigit(ch)) {
                int count = ch - '0'; // The expression ch - '0' converts the character to its numeric value.

                while (i + 1 < str.length() && Character.isDigit(str.charAt(i + 1))) {
                    // The condition Character.isDigit(str.charAt(i + 1)) checks if the next
                    // character is also a digit.
                    // If true, it continues processing the number by multiplying the current count
                    // by 10 and adding the new digit to count.

                    i++;
                    count = count * 10 + (str.charAt(i) - '0');
                }
                // retrieves the last printed letter and prints count-1 times.
                char previousChar = str.charAt(i - 1);
                for (int j = 1; j < count; j++) {
                    System.out.print(previousChar);
                }
            }
        }
    }
}

// Time Complexity --- O(N+M) where N is the length of string and M is no of
// times to print.
// Space Complexity --- O(N) used to store input String of length 'N'.