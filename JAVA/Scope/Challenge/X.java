package Java.Scope.Challenge;

import java.util.Scanner;

public class X {
    private int x;

    public X(Scanner x) {
        System.out.println("Enter a number :");
        this.x = x.nextInt();
    }

    public void x() {
        for (int x = 0; x < 11; x++) {
            System.out.println(x + " times " + this.x + " = " + x * this.x);
        }
    }
}
