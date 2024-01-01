public class SavingsAccountTest {
	    public static void main(String args[]) {
	       SavingsAccount saver1 = new SavingsAccount(0.04,2000);
	       System.out.println("saver1:");
	       saver1.calcMonthlyInterest();
	       System.out.println("After interest rate  is 5%:");
	        saver1.modifyInterestRate(0.05);
	        saver1.calcMonthlyInterest();
	        SavingsAccount saver2 = new SavingsAccount(0.04,3000);
	        System.out.println("saver2:");
		    saver2.calcMonthlyInterest();
		    System.out.println("After interest rate  is 5%:");
	        saver2.modifyInterestRate(0.05);
	        saver2.calcMonthlyInterest();
	    }
}	
