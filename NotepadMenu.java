// Notepad menu example
 
import javax.swing.*;

public class NotepadMenu {
    JFrame obj;
    JMenuBar mb; // menu bar
    JMenu file, edit, help; // menus
    JMenuItem cut, copy, paste, selectAll; // menu items
    JTextArea ta;

    NotepadMenu() {
        obj = new JFrame();
        cut = new JMenuItem("cut");
        copy = new JMenuItem("copy");
        paste = new JMenuItem("paste");
        selectAll = new JMenuItem("selectAll");
        mb = new JMenuBar();
        file = new JMenu("File");
        edit = new JMenu("Edit");
        help = new JMenu("Help");
        // adding menu items to edit menu
        edit.add(cut);
        edit.add(copy);
        edit.add(paste);
        edit.add(selectAll);
        // adding menus to menubar
        mb.add(file);
        mb.add(edit);
        mb.add(help);
        ta = new JTextArea();
        ta.setBounds(5, 5, 360, 320);
        // adding text area and menubar to frame
        obj.add(mb);
        obj.add(ta);
        obj.setJMenuBar(mb);
        obj.setLayout(null);
        obj.setSize(400, 400);
        obj.setVisible(true);
    }

    public static void main(String[] args) {

        new NotepadMenu();
    }
}

// Time Complexity --- O(1);
// Space Complexity --- O(1);