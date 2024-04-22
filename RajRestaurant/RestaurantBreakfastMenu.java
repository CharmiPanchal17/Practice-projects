
import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JTable;

public class RestaurantBreakfastMenu {
    
    public RestaurantBreakfastMenu() {
        
        JFrame frame = new JFrame("Restaurant Menu for Breakfast.");
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setVisible(true);

        JLabel label = new JLabel("You can take a look at the breakfast menu.");
        label.setFont(new Font("Times New Roman", Font.ITALIC, 20));
        label.setBounds(50, 20, 400, 30);
        frame.add(label);

        // here is a table creation.
        JTable Breakfastdata;
        String[][] data ={{"sandwitch","5000","2_pieces"},
                          {"Chappati","2000","2_pieces"},
                          {"springroll","8000","3_pieces"},
                          {"cupcakes","2500","1_pieces"},
                          {"samosas","9000","2_pieces"},
                          {"cinamon rolls","3000","3_pieces"},
                          {"dora cakes","4000","2_pieces"},
                          {"apple_pies","10,000","4_pieces"},};

        String[] columnNames = {"Item","Price","Quantity"};
        Breakfastdata = new JTable(data, columnNames);

        JScrollPane scrollPane = new JScrollPane(Breakfastdata);
        scrollPane.setBounds(50, 60, 400, 150);

        frame.add(scrollPane);


    }

    public static void main(String[] args) {
        new RestaurantBreakfastMenu();
    }
} 
    
