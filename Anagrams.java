/*Write a function to check if two strings are Anagrams without using built-in methods or sorting .*/
/*An anagram is a word or phase formed by rearranging the letters of another word or phase . Eg:"Listen --- "Slient"*/
import java.util.*;

public class Anagrams {
    public static void main(String[] args) {
        String str1="Listen";
        String str2="silent";
        isAnagrams(str1, str2);
        
    }

    public static void isAnagrams(String str1,String str2)
    {
        str1=str1.toLowerCase();
        str2=str2.toLowerCase();
        Set<Character> set1=new HashSet<>();
        Set<Character> set2=new HashSet<>();

        for(char c : str1.toCharArray())
        {
            set1.add(c);
        }
        for(char c : str2.toCharArray())
        {
            set2.add(c);
        }

        if(set1.equals(set2))
        {
          System.out.println("The given strings are Anagrams");
        }
        else
        {
            System.out.println("The given strings are not Anagrams");
        }
    }
}
