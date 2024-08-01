// Check if given year is leap year without using modulus operator 
public class LeapYear {
    public static void main(String[] args) {
        int year = 2024; // You can change this to test other years

        if (isLeapYear(year)) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }

    }

    public static boolean isLeapYear(int year) {
        // Check divisibility by 400
        if ((year / 400) * 400 == year) {
            return true;
        }

        // Check divisibility by 100
        if ((year / 100) * 100 == year) {
            return false;
        }

        // Check divisibility by 4
        if ((year / 4) * 4 == year) {
            return true;
        }

        return false;
    }
}
