
public class SavingsAccount {
    static double annualIntrestRate,savingsBalance;
    double monthlyInterest;
    SavingsAccount(double ai, double sb) {
        annualIntrestRate = ai;
        savingsBalance = sb;
    }
    public void modifyInterestRate(double ai){
        annualIntrestRate=ai;}
    public void calcMonthlyInterest() {
    	 monthlyInterest = (savingsBalance * annualIntrestRate) / 12;
        System.out.println("The Monthly interst is: $"+monthlyInterest);
        savingsBalance = savingsBalance + monthlyInterest;
        System.out.println("The total balane is: $" + savingsBalance);
    }
}
