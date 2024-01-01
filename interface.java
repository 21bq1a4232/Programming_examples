import java.util.Scanner;
interface Linear{
    void Search(int j);
}
class linear implements Linear{
    private int a[],k,c=0,flag=0;
    public linear(int size){
        a=new int[size];
        k=0;
    }
    public void add(int item){
        a[k++]=item;
    }
    public void Search(int key){
        for(int i=0;i<k;i++){    
            if(key==a[i]){
                flag=1;
                c=i;
                break;
            }
        }
        if(flag==1){
            System.out.println("element found at "+c);
            System.exit(1);
        }
        else{
            System.out.println("element not found");
        }
    }
}
class def{
    public static void main(String []args){
        linear z= new linear(8);
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("enter the size of an array:");
            int n=sc.nextInt();
            for(int i=0;i<n;i++){
                System.out.println("enter the element:");
                z.add(sc.nextInt());
            }
            System.out.println("enter the element to be found:");
            int key=sc.nextInt();
            for(int i=0;i<n;i++){
                z.Search(key);
            }
        }
    }
}