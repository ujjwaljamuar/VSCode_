public class while_loops {
    public static boolean isEvenNmber(int num){
        if((num %2)==0){
            return true;
        }
        else{
            return false;
        }
    }
    public static void main(String[] args) {
       int num=1;
       int finishNum=2051;
       int numFound=0;

       while(num <= finishNum){
           num++;
           if(!isEvenNmber(num)){
               continue;
           }
           numFound++;
           System.out.println("Even num found : "+num);
       }
       System.out.println("Total even numbers found = "+numFound);
     }
}
