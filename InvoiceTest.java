public class InvoiceTest {
    public static void main(String []args) {
        Invoice one = new Invoice("99F", "Toy", 10, 1.5);
        System.out.println("Part number: " + one.getPartNumber() + "; Part description: " + one.getPartDescription() +
                "; Sold: " + one.getQuantityOfPurchased() + "; Price: " + one.getPricePreItem() + "; Invoice amount: " +
                one.getInvoiceAmount());
        one.setPartNumber("0x000");
        one.setPartDescription("IBM");
        one.setQuantityOfPurchased(1000);
        one.setPricePreItem(1500.99);
        System.out.println("After changing:");
        System.out.println("Part number: " + one.getPartNumber() + "; Part description: " + one.getPartDescription() +
                "; Sold: " + one.getQuantityOfPurchased() + "; Price: " + one.getPricePreItem() + "; Invoice amount: " +
                one.getInvoiceAmount());
    }
}