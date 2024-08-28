
/*You are given a binary string consisting of a sequence of 1's and 0's. This binary string is an encoded version of an English Word.
 * Each uppercase letter in the world is represented by a sequence of 1's of varying lenghts , while 0's act as separators between these sequences.
 * Task is to decode the binary string and determine the original word.
 * 
 * INPUT : 11101011110
 * OUTPUT : CAD 
 */
import java.util.*;

public class BinaryString {
   public static void main(String[] args) {
      String str = "11101011110";
      System.out.println(findString(str)); // Output should be "CAD"
   }

   public static String findString(String binaString) {
      Map<String, String> alphaMap = new HashMap<>();

      // The initial value is "1"
      String base = "1";

      // Loop through the alphabet from 'A' to 'Z'
      for (char letter = 'A'; letter <= 'Z'; letter++) {
         // Add the entry to the map
         alphaMap.put(base, String.valueOf(letter));

         // Append another '1' to the base string for the next letter
         base += "1";
      }

      String res = "";
      String alphabet = "";
      for (int i = 0; i < binaString.length(); i++) {
         if (binaString.charAt(i) == '0') {
            // Add the corresponding letter to the result and reset `alphabet`
            res += alphaMap.get(alphabet);
            alphabet = ""; // Reset for the next sequence
         } else {
            alphabet += binaString.charAt(i);
         }
      }

      // Add the last sequence if there's any remaining after the loop
      if (!alphabet.isEmpty()) {
         res += alphaMap.get(alphabet);
      }

      return res;
   }
}

// Time Complexity --- O(N) where N is the length of the given input string.
// Space Complexity --- O(1).

/*
 * To solve it we can use haspmap in order to optimise the search operation ,
 * here keys will be the alphabets and corresponding values are 1's sequence
 */