package OOP2.Composition;

public class Main {
    public static void main(String[] args) {
        Dimension dimension=new Dimension(20, 20, 5);
        Case theCase=new Case("330B", "ROG", "240", dimension);
        Monitor theMonitor =new Monitor("27 inch Beast", "Asus", 27, new Resolution(3840, 2160));

        Motherboard theMotherboard=new Motherboard("Bj-200","Samsung",4,6,"v2.44");

        PC thePc=new PC(theCase,theMonitor,theMotherboard);
        thePc.powerUp();
        
    }    
}
