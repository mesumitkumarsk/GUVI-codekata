import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float f1 = sc.nextFloat();
        float f2 = sc.nextFloat();
        
        int n1 = (int) f1;
        int n2 = (int) f2;
        
        //..... YOUR CODE STARTS HERE .....
        
        int bit1 = n1 & n2; 
        int bit2 = n1 | n2; 
        int bit3 = n1 ^ n2; 
        int bit4 = ~(n1) & n2;
        
        System.out.println("Bitwise AND result: "+ bit1);
        System.out.println("Bitwise OR result: "+ bit2);
        System.out.println("Bitwise XOR result: "+ bit3);
        System.out.println("Bitwise NOT and AND result: "+ bit4);
        
        //..... YOUR CODE ENDS HERE .....
    }
}
