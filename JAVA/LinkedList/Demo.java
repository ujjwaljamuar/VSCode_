package LinkedList;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;



public class Demo {

    private static void printList(LinkedList<String> linkedList) {
        Iterator<String> i = linkedList.iterator();
        while (i.hasNext()) {
            System.out.println("Now Visiting " + i.next());
        }
        System.out.println("=============================");
    }

    private static boolean addInOrder(LinkedList<String> linkedList, String newCity) {
        ListIterator<String> stringListIterator = linkedList.listIterator();
        while (stringListIterator.hasNext()) {
            int comparison = stringListIterator.next().compareTo(newCity);

            if (comparison == 0) {
                System.out.println(newCity + " is already included as destination");
                return false;

            } else if (comparison > 0) {
                stringListIterator.previous();
                stringListIterator.add(newCity);
                return true;

            } else if (comparison < 0) {
                // move on to next city

            }
        }

        stringListIterator.add(newCity);
        return true;
    }

    private static void visit(LinkedList cities){
        Scanner sc=new Scanner(System.in);
        boolean quit= false;
        boolean goingForward=true;
        ListIterator<String> listIterator=cities.listIterator();

        if(cities.isEmpty()){
            System.out.println("No Cities in the itenerary");
            return;
        } else{
            System.out.println("Now visiting "+listIterator.next());
            printMenu();

        }
        while(!quit){
            int action=sc.nextInt();
            sc.nextLine();
            switch(action){
            case 0:
                System.out.println("Vacation Over");
                quit=true;
                break;
            case 1:
                if(!goingForward){
                    if(listIterator.hasNext()){
                        listIterator.next();
                    }
                    goingForward=true;
                }
                if(listIterator.hasNext()){
                    System.out.println("Now Visiting "+listIterator.next());
                }
                else{
                    System.out.println("Reached the end of the list");
                    goingForward=false;
                }
                break;
                
            case 2:
            if(goingForward){
                if(listIterator.hasPrevious()){
                    listIterator.previous();
                }
                goingForward=false;
            }
            if(listIterator.hasPrevious()){
                System.out.println("Now visiting "+listIterator.previous());
            }
            else{
                System.out.println("We are at start of the list.");
                goingForward=true;
            }

            case 3:
            printMenu();
            break;
            }}
        }

        private static void printMenu(){
            System.out.println("Available actions :\n press");
            System.out.println("0 - to quit \n" + "1 - to go to next city \n"+ "2 - to go to previous city\n"+"3 - to print menu options");
        }
    public static void main(String[] args) {
        LinkedList<String> placesToVisit = new LinkedList<String>();
        addInOrder(placesToVisit, "Sydney");
        addInOrder(placesToVisit, "Melbourne");
        addInOrder(placesToVisit, "Brisbane");
        addInOrder(placesToVisit, "Perth");
        addInOrder(placesToVisit, "Canberra");
        addInOrder(placesToVisit, "Adelaide");
        addInOrder(placesToVisit, "Darwin");
        printList(placesToVisit);

        addInOrder(placesToVisit, "Alice Springs");
        addInOrder(placesToVisit, "Darwin");
        printList(placesToVisit);

        visit(placesToVisit);

        // placesToVisit.add("India");
        // placesToVisit.add("London");
        // placesToVisit.add("New York");
        // placesToVisit.add("Las Vegas");
        // placesToVisit.add("Amsterdam");
        // placesToVisit.add("Switzerland");
        // placesToVisit.add("Spain");

        // printList(placesToVisit);

        // placesToVisit.add(1, "Alice Springs");

        // printList(placesToVisit);

        // placesToVisit.remove(4);
        // printList(placesToVisit);



    }
}
