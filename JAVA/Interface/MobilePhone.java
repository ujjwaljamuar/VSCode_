package Interface;


public class MobilePhone implements Itelephone {
    private int myNumber;
    private boolean isRinging;
    private boolean isOn=false;


    public MobilePhone(int myNumber) {
        this.myNumber = myNumber;
    }

    @Override
    public void powerOn() {
        isOn=true;
        System.out.println("Powering Up...");
    }

    @Override
    public void dial(int phoneNumber) {
        if(isOn){
            System.out.println("Now ringing " + phoneNumber + " on mobile phone.");
        }
        else{
            System.out.println("Phone is Switched Off..");
        }
        
    }

    @Override
    public void answer() {
        if (isRinging) {
            System.out.println("Answering the mobile phone");
        }
    }

    @Override
    public boolean callPhone(int phoneNumber) {
        if (phoneNumber == myNumber && isOn) {
            isRinging = true;
            System.out.println("Melody ring");
        } else {
            isRinging = false;
            System.out.println("Phone is not on or number is Different");
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

        ujjwalsPhone = new MobilePhone(25646);
        ujjwalsPhone.powerOn();
        ujjwalsPhone.callPhone(25646);
        ujjwalsPhone.answer();
    }
    
}