import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.*;

import java.awt.*;

public class RestaurantHome{

    public static void main(String[] args) {
        
        JFrame frame = new JFrame("Raj Restaurant");
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.getContentPane().setBackground(new Color(0xD8D8FF));


        JLabel restLogo = new JLabel(new ImageIcon("rest1.png"));
        restLogo.setBounds(165, 20, 140, 100);

        JLabel welcomLabel = new JLabel("WELCOME TO RAJ RESTAURANT");
        welcomLabel.setFont(new Font("Times New Roman", Font.ITALIC, 15));

        JPanel welcomePanel = new JPanel();
        welcomePanel.setBounds(130, 140, 230, 40);
        welcomePanel.setBackground(new Color(0x7AEB7A));
        welcomePanel.add(welcomLabel);

        JLabel forMenu = new JLabel("Click on MENU to check out our restaurant Menu");
        forMenu.setBounds(85, 200, 350, 50);
        forMenu.setFont(new Font("Ebrima", Font.PLAIN, 15));

        JButton menuButton = new JButton("MENU");
        menuButton.setBounds(200, 250, 70, 30);


        frame.add(restLogo);
        frame.add(welcomePanel);
        frame.add(forMenu);
        frame.add(menuButton);

        menuButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                if(e.getSource() == menuButton){
                    
                    new RestaurantMenu();
                    
                }
            }
        });

        frame.setVisible(true);

    }
}