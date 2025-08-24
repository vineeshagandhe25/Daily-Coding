public class ExtendedEuclidean {
    static int extenedEuclidean(int a, int b, int[] x, int[] y) {
        if (b == 0) {
            x[0] = 1;
            y[0] = 0;
            return a;
        }
        int[] x1 = new int[1];
        int[] y1 = new int[1];
        int gcd = extenedEuclidean(b, a % b, x1, y1);
        x[0] = y1[0];
        y[0] = x1[0] - (a / b) * y1[0];
        return gcd;
    }

    public static void main(String[] args) {
        int a = 30, b = 20;
        int[] x = new int[1], y = new int[1];
        int gcd = extenedEuclidean(a, b, x, y);
        System.out.println("gcd = " + gcd);
        System.out.println("x = " + x[0] + ", y = " + y[0]);
    }
}
