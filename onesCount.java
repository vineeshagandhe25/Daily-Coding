// given a array that has only 0s and 1s, and is sorted, find the no. of 1s in less then O( n ) time complexity

public class onesCount {

    public static void main(String[] args) {

        //int[] arr = {0,0,0,1,1,1,1};
        //int[] arr = {0,0,0,0};
        //int[] arr = {1,1,1,1};
        //int[] arr = {0,0,0,0};
        int[] arr = {};
        int n = arr.length;
        int low = 0, high = n-1;
        int firstIndx = -1;

        while(low <= high) {

            int mid = low + (high - low) / 2;

            if(arr[mid] == 1) {
                firstIndx = mid;
                high = mid -1;
            }
            else {
                low = mid+1;
            }
        }

        if(firstIndx == -1) {
            System.out.println(0);
        }
        else {
            System.out.println(n-firstIndx);
        }
    }
}