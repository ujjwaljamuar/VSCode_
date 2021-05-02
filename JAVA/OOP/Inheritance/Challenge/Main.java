package Inheritance.Challenge;

public class Main {
    public static void main(String[] args) {

        Outlander outlander = new Outlander(36);
        System.out.println("\n");

        outlander.steer(45);
        System.out.println("\n");

        outlander.accelerate(30);
        System.out.println("\n");

        outlander.accelerate(20);
        System.out.println("\n");

        outlander.accelerate(-42);
    }
}
