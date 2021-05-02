public class SharedDigit {
    public static boolean hasSharedDigit(int firstValue, int secondValue) {
        if (firstValue < 10 || firstValue > 99 || secondValue < 10 || secondValue > 99) {
            return false;
        }

        // A more generic solution in case we have values with more than 1 digit
//        int firstDigit, secondDigit, copySecondValue;
//        while (firstValue > 0) {
//            firstDigit = firstValue % 10;
//            copySecondValue = secondValue;
//            while (copySecondValue > 0) {
//                secondDigit = copySecondValue % 10;
//                if (firstDigit == secondDigit) {
//                    return true;
//                }
//                copySecondValue /= 10;
//            }
//            firstValue /= 10;
//        }
//        return false;

        int firstValueFirstDigit = firstValue % 10;
        int secondValueFirstDigit = secondValue % 10;
        firstValue /= 10;
        secondValue /= 10;
        int firstValueLastDigit = firstValue % 10;
        int secondValueLastDigit = secondValue % 10;
        return firstValueFirstDigit == secondValueLastDigit || firstValueFirstDigit == secondValueFirstDigit
                || firstValueLastDigit == secondValueFirstDigit || firstValueLastDigit == secondValueLastDigit;
    }

    public static void main(String[] args) {
        System.out.println("Numbers 12 and 23 has shared digits " + SharedDigit.hasSharedDigit(12, 23));
        System.out.println("Numbers 9 and 99 has shared digits " + SharedDigit.hasSharedDigit(9, 99));
        System.out.println("Numbers 15 and 55 has shared digits " + SharedDigit.hasSharedDigit(15, 55));
    }
}
