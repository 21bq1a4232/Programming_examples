import javax.swing.*;
import java.awt.*;
class Register1{
    Register1(){
        JFrame f = new JFrame("Registration");
        JLabel l1 = new JLabel("NAME :");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   
        f.setLayout(null);
        JLabel l2 = new JLabel("ROLL NO :");
        JLabel l4 = new JLabel("PHONE NO :");
        JLabel l5 = new JLabel("GENDER :");
        JLabel l6 = new JLabel("LANGUAGES KNOWN :");
        JTextField t1 = new JTextField();
        JTextField t2 = new JTextField();
        JTextArea t3 = new JTextArea(15,15);
        JTextField t4 = new JTextField();
        JRadioButton r1= new JRadioButton("Male");
        JRadioButton r2= new JRadioButton("FEMALE");
        JCheckBox c1 = new JCheckBox("Telugu");
        JCheckBox c2 = new JCheckBox("Hindi");
        JCheckBox c3 = new JCheckBox("English");
        JLabel l3 = new JLabel("ADDRESS :");
        JButton b1 = new JButton("Register");
        JButton b2 = new JButton("Cancel");
        f.add(l1);
        f.add(l2);
        f.add(l4);
        f.add(l5);
        f.add(l6);
        f.add(t1);
        f.add(t2);
        f.add(t3);
        f.add(t4);
        f.add(r1);
        f.add(r2);
        f.add(c1);
        f.add(c2);
        f.add(c3);
        f.add(b1);
        f.add(b2);
        f.add(l3);
        l1.setBounds(40, 100, 200, 40);//NAME
        t1.setBounds(90, 111, 200, 20);
        l2.setBounds(40, 130, 220, 40);//ROLL NO
        t2.setBounds(105, 141, 200, 20);
        l4.setBounds(40, 140, 260, 80);//PHONE NO
        t4.setBounds(115, 171, 200, 20);//TEXT AREA OF PHONE NO
        l5.setBounds(40, 170, 280, 100);//GENDER
        r1.setBounds(100, 211, 90, 20);//MALE
        r2.setBounds(200, 211, 120, 20);//FEMALE
        l6.setBounds(40, 190, 300, 120);//LANGUAGE
        c1.setBounds(170, 239, 70, 20);
        c2.setBounds(250, 239, 70, 20);
        c3.setBounds(330, 239, 70, 20);
        l3.setBounds(40, 269, 240, 60);//ADDRESS
        t3.setBounds(110, 269, 200, 100);//ADDRESS
        b1.setBounds(40, 400, 100, 20);
        b2.setBounds(240, 400, 100, 20);
        f.setSize(500,500);
        f.setVisible(true);
    }
    public static void main(String[] args) {
        new Register1();
    }
}