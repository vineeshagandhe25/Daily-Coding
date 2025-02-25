import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class RemoveKDigits {
    public static String removeKDigits(String num, int k) {
        if (k >= num.length()) return "0"; 

        // Convert string to character array
        char[] digits = num.toCharArray();

        // Step 1: Store original indices of each digit in a list
        List<Character> originalOrder = new ArrayList<>();
        for (char digit : digits) {
            originalOrder.add(digit);
        }

        // Step 2: Sort the digits in descending order
        List<Character> sortedDigits = new ArrayList<>(originalOrder);
        sortedDigits.sort(Comparator.reverseOrder()); // Sort in descending order

        // Step 3: Remove the first `k` largest digits
        List<Character> remainingDigits = new ArrayList<>(originalOrder);
        int removed = 0;
        for (char digit : sortedDigits) {
            if (remainingDigits.contains(digit) && removed < k) {
                remainingDigits.remove(Character.valueOf(digit));
                removed++;
            }
            if (removed == k) break;
        }

        // Step 4: Build the final number in the order of appearance in original string
        StringBuilder result = new StringBuilder();
        for (char digit : num.toCharArray()) {
            if (remainingDigits.contains(digit)) {
                result.append(digit);
                remainingDigits.remove(Character.valueOf(digit)); 
            }
        }

        // Step 5: Remove leading zeros
        while (result.length() > 1 && result.charAt(0) == '0') {
            result.deleteCharAt(0);
        }

        return result.length() == 0 ? "0" : result.toString();
    }

    public static void main(String[] args) {
        // Test cases 
        String num = "99";
        int k = 2;
        System.out.println("Smallest number after removing " + k + " digits: " + removeKDigits(num, k));

        num = "0123456789";
        k = 2;
        System.out.println("Smallest number after removing " + k + " digits: " + removeKDigits(num, k));

        num = "1234056789";
        k = 4;
        System.out.println("Smallest number after removing " + k + " digits: " + removeKDigits(num, k));

        num = "7654321";
        k = 4;
        System.out.println("Smallest number after removing " + k + " digits: " + removeKDigits(num, k));

        num = "90876";
        k = 2;
        System.out.println("Smallest number after removing " + k + " digits: " + removeKDigits(num, k));
    }
}

// Time Complexity --- in the average case O(n log n) and in the worst case O(n²).
// Space Complexity --- O(N) where N is the length of given string 

