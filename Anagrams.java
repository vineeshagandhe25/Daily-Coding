
/*Write a function to check if two strings are Anagrams without using built-in methods or sorting .*/
/*An anagram is a word or phase formed by rearranging the letters of another word or phase . Eg:"Listen --- "Slient"*/
import java.util.*;

public class Anagrams {
    public static void main(String[] args) 
    {
        String str1 = "Listen";
        String str2 = "Silent";
        if (isAnagram(str1, str2)) 
        {
            System.out.println("The given strings are anagrams");
        } 
        else 
        {
            System.out.println("The given strings are not anagrams");
        }
    }

    public static boolean isAnagram(String str1, String str2) 
    {
        // Convert strings to lower case
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        // If lengths are not equal, they cannot be anagrams
        if (str1.length() != str2.length())
        {
            return false;
        }

        // Create an array to count character frequencies
        int[] charCounts = new int[26]; // Assuming only lowercase English letters

        // Increment character counts from str1 and decrement from str2
        for (int i = 0; i < str1.length(); i++)  // Time Complexity --- O(N)
        {
            charCounts[str1.charAt(i) - 'a']++;
            charCounts[str2.charAt(i) - 'a']--;
        }

        // Check if all counts are zero I(Constant Time)
        for (int count : charCounts) 
        {
            if (count != 0) 
            {
                return false;
            }
        }

        return true;
    }
}

// Time Complexity --- O(N) where N is the length of input strings.
// Space Complexity --- O(N) where N is the length of input strings.