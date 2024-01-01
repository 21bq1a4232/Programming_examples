import java.util.Scanner;
 class BinarySearch{
	public static void main(String args[]) {
		Scanner n=new Scanner(System.in);
		System.out.println("Enter the length of array:");
		int mid,low =0,k=0,p=n.nextInt(),a[]=new int[p];
		System.out.println("Enter the elements:");
		for(int i=0; i<p ;i++)a[k++]=n.nextInt();
		int high=a.length-1;
		System.out.println("Enter the key value:");
		int key=n.nextInt();  
		   while( low <= high ){  
		       mid = (low + high)/2;  
		      if ( a[mid] < key )  low = mid + 1;     
		      else if ( a[mid] == key ){  
		        System.out.println("The Element is found at index :"+mid);
		        break;
		      }else high = mid - 1;}  
		   if ( low > high )  System.out.println("The Element not found in the given array");}}