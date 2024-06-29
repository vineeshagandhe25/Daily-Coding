//Given an array, find two numbers whose sum = k, using the hashing concept. Print indices of those two elements.

import java.util.*;
public class Hashing 
{
    public static void main(String[] args)
    {
        int arr[]={2,2,3,3,5,0,5,4,4,1};
        
        HashMap<Integer,List<Integer>> input = new HashMap<>();
        // Adding numbers as keys.
        for(int i=0;i<arr.length;i++) // Time Complexity - O(N)
        {
           
            input.put(arr[i],new ArrayList<>());
        }
        // and corresponding values are there indices in list .
        for(int i=0;i<arr.length;i++) // Time Complexity - O(N)
        {
           
            input.get(arr[i]).add(i);
        }
        
        int k=5;
        findIndices(input, k);

        
    }
   //Function to find Indices 
    public static void findIndices(HashMap<Integer,List<Integer>> map ,int k)
    {
        System.out.println("The indices are:");

        // To avoid duplicates
        Set<String> visitedPairs = new HashSet<>();

        for (Integer num1 : map.keySet()) // Time Complexity - O(N) where N is size HashMap
        {
            int num2 = k - num1;
            if (map.containsKey(num2)) 
            {
                List<Integer> li1 = map.get(num1);
                List<Integer> li2 = map.get(num2);

                for (int i : li1) // Time Complexity - O(N*M) where M is size of li1
                 {
                    for (int j : li2) // Time Complexity -O(N*M*P) where P is size of li2
                    {
                        // To avoid same element twice
                        if (i != j)
                         {
                            
                            String pair = i < j ? i + "," + j : j + "," + i; // storing pair as sting (smaller index,Larger index).
                            if (!visitedPairs.contains(pair)) 
                            {
                                visitedPairs.add(pair);
                                System.out.println(i + " " + j);
                            }
                        }
                    }
                }
            }
        }
    }
}

// Time Complexity --- O(N^2) where N is the length of array .
// Space Complexity --- O(N) where N is the length of array.