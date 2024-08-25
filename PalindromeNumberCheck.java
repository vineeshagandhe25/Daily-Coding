/**
 * Palindrome Number Check
 */
public class PalindromeNumberCheck {
    public static void main(String[] args) {
        int num = 121;
        System.out.println(isPalindrome(num));
        // corner cases 
        System.out.println(isPalindrome(1));
        System.out.println(isPalindrome(123));
        System.out.println(isPalindrome(-121));
        System.out.println(isPalindrome(1001));
        System.out.println(isPalindrome(0));
    }

    public static boolean isPalindrome(int num) {
        if (num < 0) {
            return false;
        }

        int temp = num, rev = 0;

        while (temp != 0) {
            rev = rev * 10 + temp % 10;
            temp = temp / 10;
        }

        return rev == num;
    }
}

// Time Complexity --- O(N) where N is length of given input number .
// Space Complexity --- O(1) .
