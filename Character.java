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
                int count = ch - '0'; 
               
                while (i + 1 < str.length() && Character.isDigit(str.charAt(i + 1))) {
                    i++;
                    count = count * 10 + (str.charAt(i) - '0');
                }
               
                char previousChar = str.charAt(i - 1);
                for (int j = 1; j < count; j++) {
                    System.out.print(previousChar);
                }
            }
        }
    }
}
