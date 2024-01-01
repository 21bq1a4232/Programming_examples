import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.FileWriter;-
class Register1 implements ActionListener {
    JLabel tf;
    String s1, s2, s3, s4, s5, s6, s7, s8;
    JTextField t1, t2, t4;
    JTextArea t3;
    JCheckBox c1, c2, c3;
    JRadioButton r2, r1;
    Register1() {
        JFrame f = new JFrame("Registration");
        JLabel l1 = new JLabel("NAME :");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLayout(null);
        JLabel l2 = new JLabel("ROLL NO :");
        JLabel l4 = new JLabel("PHONE NO :");
        JLabel l5 = new JLabel("GENDER :");
        JLabel l6 = new JLabel("LANGUAGES KNOWN :");
        t1 = new JTextField();
        t2 = new JTextField();
        t3 = new JTextArea(15, 15);
        t4 = new JTextField();
        r1 = new JRadioButton("Male");
        r2 = new JRadioButton("FEMALE");
        c1 = new JCheckBox("Telugu");
        c2 = new JCheckBox("Hindi");
        c3 = new JCheckBox("English");
        JLabel l3 = new JLabel("ADDRESS :");
        JButton b1 = new JButton("Register");
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
        b1.addActionListener(this);
        f.add(l3);
        tf = new JLabel();
        f.add(tf);
        l1.setBounds(40, 100, 200, 40);// NAME
        t1.setBounds(90, 111, 200, 20);
        l2.setBounds(40, 130, 220, 40);// ROLL NO
        t2.setBounds(105, 141, 200, 20);
        l4.setBounds(40, 140, 260, 80);// PHONE NO
        t4.setBounds(115, 171, 200, 20);// TEXT AREA OF PHONE NO
        l5.setBounds(40, 170, 280, 100);// GENDER
        r1.setBounds(100, 211, 90, 20);// MALE
        r2.setBounds(200, 211, 120, 20);// FEMALE
        l6.setBounds(40, 190, 300, 120);// LANGUAGE
        c1.setBounds(170, 239, 70, 20);
        c2.setBounds(250, 239, 70, 20);
        c3.setBounds(330, 239, 70, 20);
        l3.setBounds(40, 269, 240, 60);// ADDRESS
        t3.setBounds(110, 269, 200, 100);// ADDRESS
        b1.setBounds(50, 400, 100, 20);
        tf.setBounds(60, 50, 1700, 20);
        f.setSize(500, 500);
        f.setVisible(true);
    }
    public void actionPerformed(ActionEvent e) {
        tf.setText("You Are Sucessfully Registered");
        s1 = t1.getText();
        s2 = t2.getText();
        s3 = t3.getText();
        s4 = t4.getText();
        try {
            FileWriter w = new FileWriter("details.txt", true);
            w.write(s1 + "\n");
            w.write(s2 + "\n");
            w.write(s3 + "\n");
            w.write(s4 + "\n");
            w.close();
        }
        catch (Exception ae) {
            System.out.println(ae);
        }
    }
    public static void main(String[] args) {
        new Register1();
    }
}