public class FirstLastDigitSum {
    public static int sumFirstAndLastDigit(int number) {
        if (number < 0) {
            return -1;
        }

        int lastDigit = number % 10;
        while (number > 9) {
            number /= 10;
        }
        return lastDigit + number;
    }

    public static void main(String[] args) {
        System.out.println("Sum first and last digit of number 252 is " + FirstLastDigitSum.sumFirstAndLastDigit(252));
        System.out.println("Sum first and last digit of number 257 is " + FirstLastDigitSum.sumFirstAndLastDigit(257));
        System.out.println("Sum first and last digit of number 0 is " + FirstLastDigitSum.sumFirstAndLastDigit(0));
        System.out.println("Sum first and last digit of number 5 is " + FirstLastDigitSum.sumFirstAndLastDigit(5)); 
        System.out.println("Sum first and last digit of number 252 is " + FirstLastDigitSum.sumFirstAndLastDigit(252));
        System.out.println("Sum first and last digit of number -10 is " + FirstLastDigitSum.sumFirstAndLastDigit(-10));
        System.out.println("Sum first and last digit of number 10 is " + FirstLastDigitSum.sumFirstAndLastDigit(10));

    }
}
