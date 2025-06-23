public class GCD2 {

    // Function to find GCD of two numbers using the Euclidean algorithm
    public static int findGCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Function to find GCD multiple numbers
    public static int multipleGCD(int[] arr) {
        int res = arr[0];
        for(int i=1;i<arr.length;i++) {
            res = findGCD(res, i);
        }
        return res;
    }

    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9,10} ;
        multipleGCD(arr);
    }
}
