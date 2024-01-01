public class InvoiceTest {
	public static void main(String []args) {
		// This is really just a run harness to test Invoice.java	
		//This invoice should work just fine.  All inputs are positive and the expected Invoice amount is 24.95
		Invoice invoice1 = new Invoice("P000001", "Part Number 1", 5, 4.99);
		System.out.println("Standard Functionality Test.  Total Invoice should be 24.95");
		printInvoiceMessage(invoice1);	
		//In this test, I'm setting the quantity to 0 to verify that the Invoice amount is 0
		Invoice invoice2 = new Invoice("P000002", "Part Number 2", 0, 4.99);
		System.out.println("Testing 0 Quantity.  Total Invoice should be 0");
		printInvoiceMessage(invoice2);	
		//This is to test that the Quantity is set to 0 when the quanity given to the constructor is less than 0
		Invoice invoice3 = new Invoice("P000003", "Part Number 3", -2, 4.99);
		System.out.println("Testing negative Quanity.  Total Invoice should be 0");
		printInvoiceMessage(invoice3);	
		//This is to test that the Price Per Item is set to 0.0 when the price per item given to the constructor is less than 0.0
		Invoice invoice4 = new Invoice("P000004", "Part Number 4", 5, -4.99);
		System.out.println("Testing Negative Price.  Total Invoice should be 0");
		printInvoiceMessage(invoice4);	
		//Another standard functionality invoice with some larger numbers
		Invoice invoice5 = new Invoice("P000005", "Part Number 5", 72, 187.65);
		System.out.println("Standard Functionality Test with some larger numbers.  Total Invoice should be 13510.80");
		printInvoiceMessage(invoice5);	
		//Try one last one using the default constuctor and using the setter methods on variables
	}
	public static void printInvoiceMessage(Invoice invoice){
		//Just print the relevant invoice information
		System.out.printf("Invoice for Part: %s \t", invoice.getPartNumber() );
		System.out.printf("Part Description: %s \t", invoice.getPartDescription() );
		System.out.printf("Quantity: %s \t", invoice.getQuantity() );
		System.out.printf("Price Per Item: %.2f \n", invoice.getPricePerItem());
		System.out.printf("Total Invoice Amount: %.2f \n", invoice.getInvoiceAmount() );
		System.out.println("***************************************************");
		System.out.println();
	}
}