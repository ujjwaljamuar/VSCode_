package Java.AbstractClasses;

public class Penguin extends Bird{

    public Penguin(String name) {
        super(name);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void fly() {
        // TODO Auto-generated method stub
        super.fly();
        System.out.println("Hey i am not very good at fleeing , can i go for swimming instead?");
    }
    
}
