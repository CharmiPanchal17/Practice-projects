
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.*;
import java.awt.*;

// interface Restaurant{
//     void welcomepage();
//     void menu();
//     void breakfast();
//     void lunch();
//     void dinner();
//     void dessert();
//     void drinks();
    
// }

public class RajRestaurantHome{
    public static void main(String[] args){
        
        JFrame frame = new JFrame("Raj Restaurant");
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(466, 400);
        frame.getContentPane().setBackground(new Color(0xD8D8FF));

        JLabel restLogo = new JLabel(new ImageIcon("rest1.png"));
        restLogo.setBounds(165, 20, 140, 100);

        JLabel welcomeLabel = new JLabel("WELCOME TO RAJ RESTAURANT");
        welcomeLabel.setFont(new Font("Times New Roman", Font.ITALIC, 15));

        JPanel welcomePanel = new JPanel();
        welcomePanel.setBounds(130, 140, 230, 40);
        welcomePanel.setBackground(new Color(0x7AEB7A));
        welcomePanel.add(welcomeLabel);

        JLabel forMenu = new JLabel("Click on the B button for breakfast ");
        JLabel forMenu2 = new JLabel("and L and D for lunch and dinner..");

        forMenu.setBounds(110, 200, 350, 50);
        forMenu2.setBounds(110, 220, 350, 50);

        forMenu.setFont(new Font("Ebrima", Font.PLAIN, 15));
        forMenu2.setFont(new Font("Ebrima", Font.PLAIN, 15));

        JButton breakfastButton = new JButton("B-MENU");
        breakfastButton.setBounds(170, 260, 110, 30);

        frame.add(restLogo);
        frame.add(welcomePanel);
        frame.add(forMenu);
        frame.add(forMenu2);
        frame.add(breakfastButton);

        breakfastButton.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                
                if(e.getSource() == breakfastButton){
                    
                    new RestaurantBreakfastMenu();
                    
                }
            }
        });

        frame.setVisible(true);

    }
}
