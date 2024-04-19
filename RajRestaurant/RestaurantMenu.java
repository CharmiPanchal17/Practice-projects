import javax.swing.JFrame;

public class RestaurantMenu {
    
    public RestaurantMenu() {
        
        JFrame frame = new JFrame("Restaurant Menu");
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new RestaurantMenu();
    }
}
