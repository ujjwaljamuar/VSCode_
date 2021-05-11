package LinkedList;

import java.util.ArrayList;

public class Customer {
    private String name;
    private double balance;

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getBalance() {
        return this.balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
    

    public Customer(String name, double balance) {
        this.name = name;
        this.balance = balance;
    }
    public static void main(String[] args) {
        Customer customer=new Customer("Ujjwal",54.89);
        Customer anotherCustomer;
        anotherCustomer= customer;
        anotherCustomer.setBalance(12.18);
        System.out.println("Balance for customer "+ customer.getName()+ " is "+customer.getBalance());

        ArrayList<Integer> intList=new ArrayList<Integer>();
        intList.add(1);
        intList.add(3);
        intList.add(4);

        for(int i=0;i<intList.size();i++){
            System.out.println(i+" : "+intList.get(i));
        }

        intList.add(1,2);

        for(int i=0;i<intList.size();i++){
            System.out.println(i+" : "+intList.get(i));
        }

    }
}
