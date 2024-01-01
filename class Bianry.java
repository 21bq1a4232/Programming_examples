import java.util.Scanner;
class Bianry{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] A=new int[n];
        for(int i=0;i<n;i++){
            System.out.println("enter the element no"+(i+1)+":");
            A[i]=sc.nextInt();
        }
        l=a[0];
        h=a[n-1];
        while( l<=h){
            mid =(l+h)/2;
            if(a[mid]==key){
                Systen.out.println("element found at "+mid);
            }
            else if(a[mid]<key){
                l++;
            }
            else{
                h++;
            }
        }
    }
}