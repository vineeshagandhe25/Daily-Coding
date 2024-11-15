/* Write a Java program to implement a class called rational number containing four 
integer fields (Sign, numerator, denominator, exponent (raised to the power of 10)). 
Provide operations for addition, subtraction and multiplication. Keep always the 
values in lowest terms (Example: 8/12, should be represented as 2/3). Write a 
private method for conversion to lowest terms. Also provide input and output 
methods.  */

import java.util.Scanner;

public class RationalNumber {
     private int sign; // 1 for positive, -1 for negative
     private int numerator;
     private int denominator;
     private int exponent; // Represents power of 10

     // Constructor to initialize the rational number
     public RationalNumber(int sign, int numerator, int denominator, int exponent) {
          if (denominator == 0) {
               throw new IllegalArgumentException("Denominator cannot be zero.");
          }
          this.sign = sign;
          this.numerator = numerator;
          this.denominator = denominator;
          this.exponent = exponent;
          toLowestTerms();
     }

     // No-argument constructor
     public RationalNumber() {
          this.sign = 1;
          this.numerator = 0;
          this.denominator = 1;
          this.exponent = 0;
     }

     // Input method
     public void input() {
          Scanner scanner = new Scanner(System.in);

          System.out.print("Enter sign (1 for positive, -1 for negative): ");
          this.sign = scanner.nextInt();

          System.out.print("Enter numerator: ");
          this.numerator = Math.abs(scanner.nextInt());

          System.out.print("Enter denominator: ");
          this.denominator = Math.abs(scanner.nextInt());

          if (this.denominator == 0) {
               throw new IllegalArgumentException("Denominator cannot be zero.");
          }

          System.out.print("Enter exponent (power of 10): ");
          this.exponent = scanner.nextInt();

          toLowestTerms();
     }

     // Output method
     public void output() {
          System.out.println("Rational Number: " +
                    (sign < 0 ? "-" : "") + numerator + "/" + denominator + " * 10^" + exponent);
     }

     // Addition
     public RationalNumber add(RationalNumber other) {
          int lcm = lcm(this.denominator, other.denominator);
          int num1 = this.sign * this.numerator * (lcm / this.denominator);
          int num2 = other.sign * other.numerator * (lcm / other.denominator);

          int resultNumerator = num1 + num2;
          int resultSign = resultNumerator < 0 ? -1 : 1;
          return new RationalNumber(resultSign, Math.abs(resultNumerator), lcm, this.exponent);
     }

     // Subtraction
     public RationalNumber subtract(RationalNumber other) {
          other.sign *= -1; // Flip the sign of the second rational number
          return this.add(other); // Use addition to perform subtraction
     }

     // Multiplication
     public RationalNumber multiply(RationalNumber other) {
          int resultSign = this.sign * other.sign;
          int resultNumerator = this.numerator * other.numerator;
          int resultDenominator = this.denominator * other.denominator;
          int resultExponent = this.exponent + other.exponent;

          return new RationalNumber(resultSign, resultNumerator, resultDenominator, resultExponent);
     }

     // Private method to convert to lowest terms
     private void toLowestTerms() {
          int gcd = gcd(numerator, denominator);
          numerator /= gcd;
          denominator /= gcd;
     }

     // Helper method to calculate the greatest common divisor (GCD)
     private int gcd(int a, int b) {
          return b == 0 ? a : gcd(b, a % b);
     }

     // Helper method to calculate the least common multiple (LCM)
     private int lcm(int a, int b) {
          return (a * b) / gcd(a, b);
     }

     public static void main(String[] args) {
          RationalNumber r1 = new RationalNumber();
          RationalNumber r2 = new RationalNumber();

          System.out.println("Enter details for Rational Number 1:");
          r1.input();

          System.out.println("Enter details for Rational Number 2:");
          r2.input();

          System.out.println("Rational Number 1:");
          r1.output();

          System.out.println("Rational Number 2:");
          r2.output();

          System.out.println("\nAddition:");
          RationalNumber sum = r1.add(r2);
          sum.output();

          System.out.println("\nSubtraction:");
          RationalNumber diff = r1.subtract(r2);
          diff.output();

          System.out.println("\nMultiplication:");
          RationalNumber product = r1.multiply(r2);
          product.output();
     }
}
