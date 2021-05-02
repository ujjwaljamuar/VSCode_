package Inheritance;
public class Dog extends Animal {
    private int eyes;
    private int legs;
    private int tail;
    private int teeth;
    private String coat;

    

    public Dog(String name,  int size, int weight,int eyes,int legs,int tail,int teeth,String coat) {
        super(1,1, 1,1,"noway");
        this.eyes = eyes;
        this.legs = legs;
        this.tail = tail;
        this.teeth = teeth;
        this.coat = coat;
    }

    private void chew(){
        System.out.println("chew is called");
    }

    @Override
    public void eat(){
        System.out.println("eat is called");
        chew();
        super.eat();
    }

    public void walk(){
        super.move(21);
        System.out.println("walk is called");
    }

    public void run(){
        move(42);
        System.out.println("run is called");
    }

    private void moveLegs(int speed){
        System.out.println("move legs is called");
    }
    @Override
    public void move(int speed){
        System.out.println("DOG .move is called");
        moveLegs(speed);
        super.move(speed);
    }


}

