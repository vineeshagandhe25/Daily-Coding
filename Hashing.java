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
        System.out.println("The indices are :");
        for(Integer num1:map.keySet()) // Time Compleixty - O(N)
        {
            if(map.containsKey(k-num1))
            {
                int num2= k- num1;
                List<Integer> li1=map.get(num1); 
                List<Integer> li2=map.get(num2);
                Iterator<Integer> itr1=li1.iterator();  //defining iterators to list and printing value's list in order to print indices as pair. 
                Iterator<Integer> itr2=li2.iterator();
                int i = 0;
                int j = 0;

                while(itr1.hasNext() || itr2.hasNext()) // Time Compleixty - O(M) where M is maxSize(it1,itr2)
                {
                    
                    if(itr1.hasNext())
                    {
                      i=itr1.next();
                    }

                    if(itr2.hasNext())
                    {
                      j=itr2.next();
                    }

                    System.out.println(i+" "+j);
                }
            }
        } 
        
    }
}

// Time Complexity --- O(N*M) where N is the length of hashmap and M is maxSize(it1,itr2).
// Space Complexity --- O(N) where N is the length of hashmap.