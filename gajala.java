public class BinarySearch {
	public static void  Binarysearch(int low ,int high,int mid,int a[],int key) {
		mid=low+high/2;
		while(low<=high) {
			if(a[mid]==key) 
				System.out.println(mid);
			else if(a[mid]<key) 
				low=mid+1;
			else if(a[mid]>key) 
				high=mid-1;
			else
				System.out.println("element not found");
		}
		
	}
	public static void main(String args[]){
		int a[] = {91,3,54,6,3,5,56};
		int low=0;
		int high=6;
		int mid = (low+high)/2;
		int ke=5;
		Binarysearch(low,high,mid,a,ke);
		
	
		
	}
	
}