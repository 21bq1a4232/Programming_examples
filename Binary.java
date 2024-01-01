import java.util.Scanner;
class Binary{
    public static void main(String []args){
        System.out.println("enter the size of an array:");
        Scanner sc=new Scanner(System.in);
        int a[];
        int n=sc.nextInt();
        a= new int[n];
        for(int i=0;i<n;i++){
            System.out.println("enter the element:");
            a[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++){
            System.out.println(a[i]);
        }
    }
}
