import javax.swing.*;
public class UI {
    public static void main(String[] args) {
        JFrame obj = new JFrame("UI using Java Swing");
        JButton btn = new JButton("click me");
        obj.add(btn);
        obj.setBounds(500, 500, 500, 500);
        obj.setVisible(true);
    }
}
