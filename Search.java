import java.util.*;
class SearchDemo{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
            System.out.println("enter the size of array:");
            int n=s.nextInt();
            int[] a=new int[10];
            for(int i=0;i<n;i++){
                a[i]=s.nextInt();
            }
            int key =s.nextInt();
            int f=0;
            int c=0;
            for(int i=0;i<n;i++){
                if (key==a[i]){
                    f=1;
                    c=i;
                }
                else{
                    continue;
                }
            }
            if (f==1){
                System.out.println("element found at "+c);
            }
            else{
                System.out.println("not found");
            }
    }
}