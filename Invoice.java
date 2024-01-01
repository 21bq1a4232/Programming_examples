public class Invoice {
    private String partNumber;
    private String partDescription;
    private int quantityOfPurchased;
    private double pricePreItem;

    public Invoice(String partNumber, String partDescription, int quantityOfPurchased, double pricePreItem) {
        this.partNumber = partNumber;
        this.partDescription = partDescription;
        this.quantityOfPurchased = quantityOfPurchased;
        this.pricePreItem = pricePreItem;
    }

    public void setPartNumber(String partNumber) {
        this.partNumber = partNumber;
    }

    public String getPartNumber() {
        return partNumber;
    }

    public void setPartDescription(String partDescription) {
        this.partDescription = partDescription;
    }

    public String getPartDescription() {
        return partDescription;
    }

    public void setQuantityOfPurchased(int quantityOfPurchased) {
        if (quantityOfPurchased > 0) {
            this.quantityOfPurchased = quantityOfPurchased;
        } else {
            this.quantityOfPurchased = 0;
        }
    }

    public int getQuantityOfPurchased() {
        return quantityOfPurchased;
    }

    public void setPricePreItem(double pricePreItem) {
        if (pricePreItem > 0) {
            this.pricePreItem = pricePreItem;
        } else {
            this.pricePreItem = 0;
        }
    }

    public double getPricePreItem() {
        return pricePreItem;
    }

    public double getInvoiceAmount() {
        return pricePreItem * quantityOfPurchased;
    }
}

class InvoiceTest {
    public static void main(String[] args) {
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