package Ecapsulation.Challenge;

public class Printer {
    private int tonerLevel;
    private int pagesPrinted;
    private boolean duplex;

    public Printer(int tonerLevel, boolean duplex) {
        if(tonerLevel >-1 && tonerLevel <=100){
            this.tonerLevel = tonerLevel;
        }
        else{
            this.tonerLevel=-1;
        }
        this.duplex = duplex;
        this.pagesPrinted=0;
    }
    
    public int addToner(int tonerAmount){
        if(tonerAmount >0 && tonerAmount <=100){
            if(this.tonerLevel+tonerAmount >100){
                return -1;
            }

            this.tonerLevel += tonerAmount;
            return this.tonerLevel;
        } else{
            return -1;
        }
    }

    public int printPages(int pages){
        int pagestoPrint=pages;
        if(this.duplex){
            pagestoPrint /=2;
            System.out.println("Printing in duplex Mode.");
        }
        this.pagesPrinted += pagestoPrint;
        return pagestoPrint;
    }


    public int getPagesPrinted() {
        return this.pagesPrinted;
    }

}
