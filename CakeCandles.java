/*Problem: Birthday Cake Candles
You are in charge of a birthday celebration, and you have a cake with candles on it. Each candle has a specific height. 
When you blow out the candles, you can only blow out the tallest ones. Your task is to find out how many candles can be blown out.

Input: An array of integers representing the height of each candle on the cake.
Output: Return an integer representing the number of candles that are the tallest. */

public class CakeCandles {
    public static void main(String[] args) {
        int arr[] = { 4, 4, 1, 3 };
        System.out.println("The no of candles can blow are :" + findCandles(arr));
        // edge cases
        int arr1[] = {};
        System.out.println("The no of candles can blow are :" + findCandles(arr1));
    }

    public static int findCandles(int arr[]) {

        if (arr.length == 0)
            return 0; // Handle edge case for empty array
        int res = 0;
        int height = 0;
        for (int i = 0; i < arr.length; i++) {
            if (height < arr[i]) {
                height = arr[i];
                res = 1;
            } else if (height == arr[i]) {
                res++;
            }
        }
        return res;
    }
}

// Time Complexity --- O(N) where N is the length of given array.
// Space Complexity --- O(1).