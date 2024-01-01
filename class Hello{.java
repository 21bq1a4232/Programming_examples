public class Invoice {
    String partNumber;
    String partDescription;
    int quantityOfPurchased;
    double pricePreItem;
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
    publicvoid setPartDescription(String partDescription) {
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