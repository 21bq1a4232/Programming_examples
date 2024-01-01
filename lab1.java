import java.uitl.Scanner;
class Invoice{
    private String pnum; 
    private String pdes; 
    private int quantity; 
    private double price;
    public String getPnum(){
        return pnum;
    }
    public void setPnum(String pnum){
        this.pnum=pnum;
    }
    public String getpdes(){
        return pdes;
    }
    public void setPdes(String pdes){
        this.pdes=pdes;
    }
    public int getQuantity(){
        return quantity;
    }
    public void setQuantity(int quantity){
        this.quantity=quantity;
    }
    public double getprice(){
        return price;
    }
    public void setPrice(double price){
        this.price=price;
    }
    double getInvoiceAmount(){
        if(quantity<0 || price<0){
            return 0.0;
        }
        else{
            return quantity*price;
        }
    }
}
class InvoiceTest{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Invoice i = new Invoice();
        System.out.println("Enter part NUmber:");
        i.setPnum(sc.next());
        System.out.println("Enter the part discription :");
        i.setPdes(sc.next());
        System.out.println("Enter the Quantity:");
        i.setQuantity(sc.nextInt());
        System.out.println("Enter the price:");
        i.setPrice(sc.nextDouble());
        System.out.println("the amount= "+i.getInvoiceAmount());
        sc.close();
    }
}