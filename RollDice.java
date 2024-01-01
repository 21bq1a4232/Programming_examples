import java.util.Random;
public class RollDice{
	public static void main( String[ ] args){
		Random randomNumbers = new Random( ); 
		int frequency1 = 0; 
		int frequency2 = 0; 
		int frequency3 = 0; 
		int frequency4 = 0; 
		int frequency5 = 0; 
		int frequency6 = 0; 
		int face1,face2; 
		for ( int roll = 1; roll <= 10000; roll++ )
		{ 
			face1 = 1 + randomNumbers.nextInt( 6 ); 
			face2 = 1 + randomNumbers.nextInt( 6 ); 
			if(face1==face2){
				switch(face1)
				{
					case 1:	++frequency1; 
							break;
					case 2:	++frequency2; 
							break;
					case 3:	++frequency3; 
							break;
					case 4:	++frequency4; 
							break;
					case 5:	++frequency5; 
							break;
					case 6:	++frequency6; 
							break; 
				}
			} 
		} 
		System.out.println( "Face\tFrequency" ); // output headers
		System.out.printf("1\t%d\n2\t%d\n3\t%d\n4\t%d\n5\t%d\n6\t%d\n" ,
		frequency1, frequency2, frequency3, frequency4,frequency5, frequency6 );
	} 
}