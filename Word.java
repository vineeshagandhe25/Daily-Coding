// Given an odd length word which should be printed from the middle of the word.
public class Word {
    public static void main(String[] args) {
        String str = "program";
        printWord(str);
    }

    public static void printWord(String str) {
        int startIndex = str.length() / 2 ;  // getting middle letter of given string

        for (int i = startIndex; i < str.length(); i++) {  // printing from mid index to last index
            System.out.print(str.charAt(i));
        }

        for (int i = 0; i < startIndex; i++) {  // following by printing from first index to mid index
            System.out.print(str.charAt(i));
        }
    }
}


// Time Complexity --- O(N) where N is the length of string.
// Space Complexity --- O(1)