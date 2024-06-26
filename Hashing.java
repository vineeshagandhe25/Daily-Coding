//Given an array, find two numbers whose sum = k, using the hashing concept. Print indices of those two elements.

import java.util.*;
public class Hashing 
{
    public static void main(String[] args)
    {
        int arr[]={2,3,3,8,9};
        
        HashMap<Integer,List<Integer>> input = new HashMap<>();
        // Adding numbers as keys.
        for(int i=0;i<arr.length;i++)
        {
           
            input.put(arr[i],new ArrayList<>());
        }
        // and corresponding values are there indices in list format .
        for(int i=0;i<arr.length;i++)
        {
           
            input.get(arr[i]).add(i);
        }
        
        int k=5;
        findIndices(input, k);
        
    }
   //Function to find Indices 
    public static void findIndices(HashMap<Integer,List<Integer>> map ,int k)
    {
        System.out.println("The indices are :");
        for(Integer num1:map.keySet())
        {
            if(map.containsKey(k-num1))
            {
                int num2= k- num1;
                System.out.println(map.get(num1)+" "+map.get(num2));
            }
        }
        
    }
}

// Time Complexity --- O(N) where N is the length of array.
// Space Complexity --- O(N) where N is the length of array.