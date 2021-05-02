package OOP2.Composition;

public class Motherboard {
    private String model;
    private String manufacturer;
    private int ramSlot;
    private int cardslots;
    private String bios;    

    public void loadProgram(String programName){
        System.out.println("Program "+programName+" is now loading....");
    }

    public String getModel() {
        return this.model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getManufacturer() {
        return this.manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public int getRamSlot() {
        return this.ramSlot;
    }

    public void setRamSlot(int ramSlot) {
        this.ramSlot = ramSlot;
    }

    public int getCardslots() {
        return this.cardslots;
    }

    public void setCardslots(int cardslots) {
        this.cardslots = cardslots;
    }

    public String getBios() {
        return this.bios;
    }

    public void setBios(String bios) {
        this.bios = bios;
    }

    public Motherboard(String model, String manufacturer, int ramSlot, int cardslots, String bios) {
        this.model = model;
        this.manufacturer = manufacturer;
        this.ramSlot = ramSlot;
        this.cardslots = cardslots;
        this.bios = bios;
    }
}
