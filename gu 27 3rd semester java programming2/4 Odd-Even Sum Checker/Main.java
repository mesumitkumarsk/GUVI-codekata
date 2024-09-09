import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
            //..... YOUR CODE STARTS HERE .....
            
            int n = scanner.nextInt();
            int[] arr = new int[n];
            for(int i=0; i<n; i++){
                int element = scanner.nextInt(); 
                arr[i] = element; 
            }

            int oddSum=0, evenSum=0; 

            for(int i=0; i<n; i++){
                if(arr[i]%2==0){
                    evenSum+=arr[i];
                } else { 
                    oddSum+=arr[i];
                }
            }

            if(evenSum>oddSum){ 
                System.out.println("Even Sum Greater");
            } else if(evenSum==oddSum){
                System.out.println("Equal");
            } else { 
                System.out.println("Odd Sum Greater");
            }
            
            
            //..... YOUR CODE ENDS HERE .....
    }
}
