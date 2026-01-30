import java.util.*;

public class Intersection {
    
    public static void main(String[] args) {
        int[] A = {1, 2, 2, 3, 4};
        int[] B = {2, 2, 4, 6};
        int i = 0, j= 0;

        ArrayList<Integer> res = new ArrayList<>();

        while (i < A.length && j < B.length) {
            if(A[i] == B[j]) {
                res.add(A[i]);
                i++;
                j++;
            }
            else if(A[i] < B[j]) {
                i++;
            }
            else {
                j++;
            }
        }

        for(int n : res) {
            System.out.println(n);
        }

    }
}
