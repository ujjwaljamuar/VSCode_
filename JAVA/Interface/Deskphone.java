package Interface;

public class Deskphone implements Itelephone {
    private int myNumber;
    private boolean isRinging;


    public Deskphone(int myNumber) {
        this.myNumber = myNumber;
    }

    @Override
    public void powerOn() {
        System.out.println("No action take, no power button.");
    }

    @Override
    public void dial(int phoneNumber) {
        System.out.println("Now ringing " + phoneNumber + " on deskphone.");
    }

    @Override
    public void answer() {
        if (isRinging) {
            System.out.println("Answering the phone");
        }
    }

    @Override
    public boolean callPhone(int phoneNumber) {
        if (phoneNumber == myNumber) {
            isRinging = true;
            System.out.println("Ring ring");
        } else {
            isRinging = false;
        }
        return false;
    }

    @Override
    public boolean isRinging() {

        return isRinging;
    }
    public static void main(String[] args) {
        Itelephone ujjwalsPhone;
        ujjwalsPhone = new Deskphone(80835281);
        ujjwalsPhone.powerOn();
        ujjwalsPhone.callPhone(80835281);
        ujjwalsPhone.answer();
    }
}
