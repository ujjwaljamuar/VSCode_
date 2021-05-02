import java.util.*;

public class switch_case {

    private static void printDayoftheWeek(int day) {
        switch (day) {
        case 0:
            System.out.println("Sunday");
            break;

        case 1:
            System.out.println("Monday");
            break;

        case 2:
            System.out.println("Tuesday");
            break;

        case 3:
            System.out.println("Wednesday");
            break;

        case 4:
            System.out.println("Thursday");
            break;

        case 5:
            System.out.println("Friday");
            break;

        case 6:
            System.out.println("Saturday");
            break;
        default:
            System.out.println("Invalid input.");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the num: ");
        int day = sc.nextInt();
        printDayoftheWeek(day);
        sc.close();
    }

}
