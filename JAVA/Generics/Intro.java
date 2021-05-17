package Java.Generics;

import java.util.ArrayList;

public class Intro {
    public static void main(String[] args) {
        ArrayList<Integer> items = new ArrayList<Integer>(); /* if we remove the <Integer> in this code it will show
                                                              warnings because java doesnot know what will i put in
                                                              the arraylist */
        items.add(1);
        items.add(2);
        items.add(3);
        items.add(4);
        items.add(5);

        printDOubled(items);

    }

    private static void printDOubled(ArrayList<Integer> n) {
        for (int i : n) {
            System.out.println("Doubled is "+ i * 2);
        }
    }

}
