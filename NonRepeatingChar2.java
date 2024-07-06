/*Given a string S of lowercase english letters, the task is to find the inndex of the first non repeating character.If there is no such character , return -1 */

import java.util.*;
public class NonRepeatingChar2
{
   public static void main(String[] args)
   {
    String s = "vineesha";
    int index = nonRepeatingChar(s);
    System.out.println("The index of first non repeating character is " + index);
   }

   public static int nonRepeatingChar(String S) 
    {

        Map<Character,Integer> charCounts = new HashMap<>();

        // Key is character and corresponding value is their frequency.
        for (int i = 0; i < S.length(); i++) // Time Complexity --- O(N)
        {
           charCounts.put(S.charAt(i),charCounts.getOrDefault(S.charAt(i),0)+1); 
        }
        // Check if any count is 1
        for (int i = 0; i < S.length(); i++) // Time Complexity --- O(N)
        {
            if (charCounts.get(S.charAt(i))== 1) 
            {
                return i;
            }
        }
        return -1;
    }   
}
// Time Complexity --- O(N) where N is length of input string;
// Space Complexity --- O(N) where N is length of input string;
