package Java.AbstractClasses;

public class Main {

    public static void main(String[] args) {
	    Dog dog = new Dog("Yorkie");
        dog.breathe();
        dog.eat();

        Eagle eagle = new Eagle("Australian ringneck");
        eagle.breathe();
        eagle.eat();
        eagle.fly();

        Penguin penguin = new Penguin("Emperor");
        penguin.fly();

        
        String stringData = "Darwin Brisbane Perth Melbourne Canberra Adelaide Sydney Canberra";

        String[] data = stringData.split(" ");
        for (String s : data) {
            // create new item with value set to the string s

        }
    }
}
