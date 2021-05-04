package Ecapsulation;

public class Main{
    public static void main(String[] args) {
        // Player player=new Player();
        // player.name="Sakshi";
        // player.health=20;
        // player.weapon="Spear";

        // int damage=10;
        // player.loseHealth(damage);
        // System.out.println("Remaining Health : "+player.healthRemaining());

        // damage=11;
        // player.health=200;
        // player.loseHealth(damage);
        // System.out.println("Remaining Health : "+player.healthRemaining());

        EnhancedPlayer player=new EnhancedPlayer("Ujjwal", 50, "UZI");
        System.out.println(player.getName()+" is Playing .");
        System.out.println("Initial Health is "+player.getHealth()+ ".");
        

    }
}