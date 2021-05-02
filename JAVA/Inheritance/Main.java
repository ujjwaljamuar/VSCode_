package Inheritance;
public class Main {
    public static void main(String[] args) {
        Animal animal=new Animal(1,1,5,5,"Animal");

        Dog dog=new Dog("Husky",8,20,2,4,1,20,"long silky");
        dog.eat();
        dog.walk();
        dog.run();

    }    
}
