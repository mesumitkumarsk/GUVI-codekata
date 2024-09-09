import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        
        //..... YOUR CODE STARTS HERE .....

        int p = (a+b)*c; 
        int q = (b-d)/a;
        int r = (a*d)+c;
        int s = (a+b+c+d)/2;
        
        System.out.println("Result of operation 1: "+ p);
        System.out.println("Result of operation 2: "+ q);
        System.out.println("Result of operation 3: "+ r);
        System.out.println("Result of operation 4: "+ s);
    
        //..... YOUR CODE ENDS HERE .....
    }
}
