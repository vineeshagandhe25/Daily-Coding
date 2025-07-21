/*Given an array of positive integers arr[] and an integer k, you can remove either the leftmost or rightmost element from the array in one operation. 
After each operation, the size of arr[] is reduced by one. The task is to find the minimum number of operations required to make the total sum of the 
removed elements exactly equal to k. If it is impossible to achieve the sum k, return -1. */

import java.util.HashMap;
import java.util.Map;

public class MinRemovals {
    static int minRemovals(int[] arr, int k) {
        int total = 0;
        int n = arr.length;
        for(int num : arr) {
            total += num;
        }
        int target = total - k;
        if(target == k) return n;
        Map<Integer,Integer> mp = new HashMap<>();
        int ps = 0;
        int maxlength = -1;
        for(int i =0;i<n;i++) {
            ps += arr[i];
            if(ps == target) maxlength += i+1;
            else if(mp.containsKey(ps-target)) {
                maxlength = Math.max(maxlength,i-mp.get(ps-target));
            }
            if(!mp.containsKey(ps)) mp.put(ps,i);
        }
        return maxlength == -1 ? -1: n-maxlength; 
    }

    public static void main(String[] args) {
        int[] arr = {3, 4, 1, 3, 2};
        int k = 5;
        System.out.println(minRemovals(arr, k));
    }
}
