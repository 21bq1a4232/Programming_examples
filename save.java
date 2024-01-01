import java.util.Scanner;
class lab {
	public static void main(String []args){
		System.out.println("enter the size of an array:");
		Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new Int[n];
        for(int i=0;i<n;i++){
            System.out.println("enter the element: ");
            a[i]=sc.nextInt();
        }
        System.out.println("enter the element to be found:");
        int key=sc.nextInt();
        int l=0;
        int h=a.length-1;
        while(l<=h){
            mid=(l+h)/2;
            for(int i=0;i<n;i++){
                if (a[mid]==key){
                    System.out.println("element found at: "+mid);
                }
                else if(a[mid]<key){
                l=mid+1;
                }
                else{
                    h=mid-1;
                }
            }
        }
	}
}