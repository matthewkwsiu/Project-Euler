import java.util.HashSet;

//NOTE! this is code for java

public class simulation {
    public static int totalSum=0;
    
    public static void main(String args[]) {


       for(int i=0; i<1000; i++){
            if(i%3==0) {
                totalSum = totalSum + i;
                System.out.println(i);
            }
            else
                if(i%5==0) {
                    totalSum = totalSum + i;
                    System.out.println(i);
                }
       }

       System.out.println(totalSum);

    }
}
