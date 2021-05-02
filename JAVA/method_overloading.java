public class method_overloading {

    public static double calfeetandinchestocen(double feet,double inches){
        if((feet< 0) || ((inches < 0) || (inches > 12))){
            System.out.println("Invalid");
            return -1;
        }
        double centimeters=(feet*12) * 2.54;
        centimeters += inches *2.54;
        System.out.println(feet+" feet ," + inches + " inches = "+centimeters + " cm");
        return centimeters;
    }

    public static double calfeetandinchestocen(double inches){
        if(inches < 0){
            System.out.println("Invalid inputs");;
            return -1;
        }
        double feet=(int) inches/12;
        double remainingInches= (int) inches % 12;
        System.out.println(inches+" inches equal to "+feet+" feet and "+remainingInches+ " inches.");
        return calfeetandinchestocen(feet, remainingInches);
    }
    
    
    public static void main(String[] args) {
      calfeetandinchestocen(170);
    }
    
}
