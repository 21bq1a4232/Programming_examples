public class InvoiceTest{
public static void main(String[] args){
        // Create Object(s)
        Invoice object1 = new Invoice(“27”, “Blueberry parfait”, 3, 9.9);
        Invoice object2 = new Invoice(“12”, “Rainbow Fraffucino”, 5, 6.6);
        Invoice object3 = new Invoice(“94”, “Strawberry shortcake”, 7, 29.8);
        // Print the Invoice
        System.out.println(“This is an Invoice for the Item(s) Sold:” + “\n”);
        System.out.println(object1.getNumber() + “\t” + object1.getDescription() + “\t” + object1.getQuantity() + “\t” + object1.getPrice() + “\t” + object1.getInvoiceAmount());
        System.out.println(object2.getNumber() + “\t” + object2.getDescription() + “\t” + object2.getQuantity() + “\t” + object2.getPrice() + “\t” + object2.getInvoiceAmount());
        System.out.println(object3.getNumber() + “\t” + object3.getDescription() + “\t” + object3.getQuantity() + “\t” + object3.getPrice() + “\t” + object3.getInvoiceAmount());
        System.out.println(“\n”);
        double total = object1.getInvoiceAmount() + object2.getInvoiceAmount() + object3.getInvoiceAmount();
        System.out.println(“TOTAL: “+ total + “\n\n”);
    }
}