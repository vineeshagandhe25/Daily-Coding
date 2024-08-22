// Convert a string to an integer .
public class StringToNum {
    public static void main(String[] args) {
        String str = "1234";
        int num = convert(str);
        System.out.println("Converted number: " + num);
    }

    public static int convert(String str) {
        int result = 0;
        for (int i = 0; i < str.length(); i++) {
            // Convert each character to its numeric value and add it to the result
            result = result * 10 + (str.charAt(i) - '0');
        }
        return result;
    }
}

// Time Complexity --- O(N) where N is the length of the given input string.
// Space Complexity --- O(1).

/*To convert character to its corresponding numeric value, we subtract '0':

str.charAt(i) - '0':
Suppose str.charAt(i) returns '3'.
'3' has an ASCII value of 51.
'0' has an ASCII value of 48.
Subtracting these gives we get `51 - 48 = 3 */