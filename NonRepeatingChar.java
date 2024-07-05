/*Given a string S of lowercase english letters, the task is to find the inndex of the first non repeating character.If there is no such character , return -1 */

public class NonRepeatingChar 
{
    public static void main(String[] args)
    {
        String s = "vineesha";
        int index = nonRepeatingChar(s);
        System.out.println("The index of first non repeating character is " + index);
    }

    public static int nonRepeatingChar(String S) 
    {

        int[] charCounts = new int[26]; // Assuming only lowercase English letters

        // Increment character counts
        for (int i = 0; i < S.length(); i++) // Time Complexity --- O(N)
        {
            charCounts[S.charAt(i) - 'a']++;
        }

        // Check if any count is 1
        for (int i = 0; i < S.length(); i++) // Time Complexity --- O(N)
        {
            if (charCounts[S.charAt(i) - 'a'] == 1) 
            {
                return i;
            }
        }
        return -1;
    }
}
// Time Complexity --- O(N) where N is length of input string;
// Space Complexity --- O(1) because we use a fixed-size array (26 elements);