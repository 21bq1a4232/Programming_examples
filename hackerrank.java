import java.util.Scanner;

public class hackerrank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the value: ");
        int a = sc.nextInt();
        int n = sc.nextInt();
        int s=0;
        for(int i=1;i<n;i++){
            s=s+(int)Math.pow(a,i);
        }
        System.out.println(s);
    }
}
