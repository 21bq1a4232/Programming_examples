import javax.swing.*;
class Registration{
    Registration(){
        JFrame f = new JFrame("Registration");
        f.setSize(500,500);
        f.setDefaultCloseOperation(1);
        JLabel l1 = new JLabel("REGISTRATION FORM");
        f.setVisible(true);
    }
    public static void main(String[] args) {
        new Registration();
    }
}