import java.util.Scanner;
public class BinSearchDemo {

	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		System.out.println("Enter size of array:");
		int size=s.nextInt();
		System.out.println("Enter elements:");
		BinSearch ob=new BinSearch(size);
		for(int i=0; i<size;i++) {
			ob.add(s.nextInt());
		}
		System.out.println("Enter key:");
		int key=s.nextInt();
		ob.bin(key);
		
	}

}

