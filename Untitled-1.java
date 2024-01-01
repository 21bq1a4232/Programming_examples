import javax.swing.*;
class gui{
    public static void main(String[] args) {
        JFrame f = new JFrame("wiuchuiqwhcweic");
        JButton b = new JButton("click Me");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().add(b);
        f.setSize(500,500);
        f.setVisible(true); 
    }
}