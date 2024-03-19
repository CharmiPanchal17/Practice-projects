import random
import getpass
import time

# MAIN FUNCTIONS AND THE CLASS FOR THE USER AND THE COMP INPUTS
class Game_Rock_Paper_Scissors_Computer:
    def __init__(self) :
        self.choices = ["rock", "paper", "scissors"]
        # polymorphism
        self.load_scores_comp()
       

    # appending to the score_comp.txt file when player choses to play with computer
    def load_scores_comp(self):
        try:
            with open("score_comp.txt", "r+") as file:
                scores = file.readlines()
    
                if len(scores) >= 3:
                    self.wins = int(scores[0].strip())
                    self.losses = int(scores[1].strip())
                    self.ties = int(scores[2].strip())

                    
                else:
                    self.wins = 0
                    self.losses = 0
                    self.ties = 0
                    
        # error handling
        except FileNotFoundError:
            self.wins = 0
            self.losses = 0
            self.ties = 0
            print("File Not found!")
            
    # writting to score_comp.txt
    def save_scores_comp(self):
        with open("score_comp.txt", "w+") as file:
            file.write(f"WINS | {self.wins} |")
            file.write(f" LOSES | {self.losses} |")
            file.write(f" DRAWS | {self.ties} |")

    # Player choice to pick from the list self.choices
    def get_player_choice(self):
        while True:
            player_choice = input("> Enter your choice (rock, paper, scissors) >: ").lower()
            if player_choice in self.choices:
                return player_choice
            else:
                print("Invalid choice. Please enter (rock, paper, scissors). ")
    
    # Computer choice to pick from the list self.choices but on random
    def get_computer_choice(self, difficulty):
        # difficulty level --------------------------------
        if difficulty == "easy":
            print(f"You chose difficulty level: {difficulty}")
            return random.choice(self.choices)
            
        elif difficulty == "medium":
            # making the computer to win more often 50%
            print(f"You chose difficulty level: {difficulty}")
            choice_with_bias = ["paper", "scissors"]
            return random.choice(choice_with_bias)

        elif difficulty == "hard":
            # making the computer to always win more often 80%
            print(f"You chose difficulty level: {difficulty}")
            
            if self.wins > self.losses:
                return random.choice(["paper", "scissors"])
            else:
                return random.choice(["rock", "paper", "scissors"]) 
        
        else:
            raise ValueError("Invalid difficulty level. please choose (easy, medium, hard).")
        # ---------------------------------------------------
class Main1(Game_Rock_Paper_Scissors_Computer):
    # a function which will determine the winner if the choices are the same or different
    def determine_winner_comp(self, player_choice, computer_choice): 
        if player_choice == computer_choice:
            # concatinating
            self.ties += 1
            return "It is a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors"):
            self.wins += 1
            return "You win!, Rock crushes scissors!"
        elif (player_choice == "paper" and computer_choice == "rock"):
            self.wins += 1
            return "You win!, Paper covers rock!"
        elif (player_choice == "scissors" and computer_choice == "paper"):
            self.wins += 1
            return "You win!, Scissors cuts paper!"
        else:
            self.losses += 1
            return "Computer wins, you lose!"

    def play_with_computer(self):
        while True:
            print("\n")
            print(" ☆☆☆☆☆☆☆☆☆☆☆ L E T 'S P L A Y ! ☆☆☆☆☆☆☆☆☆☆☆ ")
            print("---------------------------------------------")
            user_input = input("Would you like to start the game? (yes/no): ").lower()
            
            if user_input != "yes":
                print("Its fine if you dont want to play")
                print("------------------------------------------")
                break
            
            print("\n")
            print("Welcome to this wonderful adventure of Rock Paper Scissors! 🏕️🏝️🏖️🏕 \n")
            print("Starting...\n")
            time.sleep(1)  # Adding delays for extra effects
            print("Please wait!")
            time.sleep(1)
            difficulty = input("Choose difficult level (easy, medium, hard): ").lower()
            if difficulty not in ["easy","medium","hard"]:
                print("Invalid difficulty level. Please select on the levels above.")
                continue
            
            num_rounds = int(input("How many rounds do you want to play: "))
            
            for round in range(1, num_rounds + 1):
                print(f"\nRound {round}:")
                player_choice = self.get_player_choice()
                computer_choice = self.get_computer_choice(difficulty)
                print(f"\nYou chose: {player_choice}")
                print(f"Computer chose: {computer_choice}")
                print(self.determine_winner_comp(player_choice, computer_choice))
                
              
            print("\nGame Over!")
            
            self.save_scores_comp()
            # reading from the score_comp.txt
            print("---------------- SCORES -------------------")
            
            with open("score_comp.txt", "r") as file:
                scores = file.read()
            print(scores)
            
            print(" ------------------------------------------")
                 
                 
                 
                 
            print(f"Rounds: {num_rounds}, Wins: {self.wins}, Loses: {self.losses}, Draws: {self.ties}")
            
            if self.wins > self.losses:
                # emojis 
                emoji = "\U0001F600"
                print("You are on a wining streak! keep it up", emoji)
            elif self.losses > self.wins:
                # emojis 
                emoji = "\U0001F62A"
                print("The computer seems to have your number. Can you turn the tide?", emoji)
            else:
                # emojis 
                emoji = "\U0001F923"
                print("Its neck and neck! Keep playing to see who comes out on top.", emoji)
            
            print("---------------------------------------------")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing, COME BACK AGAIN")
                print("------------------------------------------")
                break

class Game_Rock_Paper_Scissors_Friend:
    def __init__(self) :
        self.choices = ["rock", "paper", "scissors"]
        # polymorphism
        self.load_scores_friend()
       
    #appending the scores to file when player choses to play with a friend
    def load_scores_friend(self):
        try:
            with open("score_friend.txt", "r+") as file:
                scores = file.readlines()
    
                if len(scores) >= 3:
                    self.player1_wins = int(scores[0].strip())
                    self.player2_wins = int(scores[1].strip())
                    self.draws = int(scores[2].strip())

                    
                else:
                    self.player1_wins = 0
                    self.player2_wins = 0
                    self.draws = 0
                    
        # error handling
        except FileNotFoundError:
            self.player1_wins = 0
            self.player2_wins = 0
            self.draws = 0
            print("File Not found!")
            
    # writting to score_friend.txt
    def save_scores_friend(self):
        with open("score_friend.txt", "w+") as file:
            file.write(f"PLAYER_1 WINS | {self.player1_wins} |")
            file.write(f" PLAYER_2 WINS | {self.player2_wins} |")
            file.write(f" DRAWS | {self.draws} |")

class Main2(Game_Rock_Paper_Scissors_Friend):
    def __init__(self):
        self.player1_wins=0
        self.player2_wins=0
        self.draws=0
        self.choices = ["rock", "paper", "scissors"]


    def player_choices(self):
        while True:
            player_choice = getpass.getpass("> Enter your choice (rock, paper, scissors) >: ").lower()
            if player_choice in self.choices:
                return player_choice
            else:
                print("Invalid choice. Please enter (rock, paper, scissors). ")

    def determine_winner_friend(self, player_1_choice, player_2_choice, player_1_name, player_2_name):
        if player_1_choice == player_2_choice:
            self.draws += 1
            return "It is a tie"

        elif (player_1_choice == "rock" and player_2_choice == "scissors"):
            self.player1_wins += 1
            return f"{player_1_name} wins!"

        elif (player_1_choice == "paper" and player_2_choice == "rock"):
            self.player2_wins += 1
            return f"{player_1_name} wins!"

        elif (player_1_choice == "scissors" and player_2_choice == "paper"):
            self.player1_wins += 1
            return f"{player_1_name} wins!"

        else:
            self.player2_wins += 1
            return f"{player_2_name} wins"


    def play_with_friend(self): 
        
        while True:
            
            print("\n")
            print("☆☆☆☆☆☆☆☆☆☆☆ L E T 'S   P L A Y   T O G E T H E R ! ☆☆☆☆☆☆☆☆☆☆☆ ")
            print("\n")
            player_1_name = input("Please enter username of player 1: ")
            player_2_name = input("Please enter username of player 2: ")
            
            print(f"\n{player_2_name}, Please look away...! Let {player_1_name} enter...")
            player_1_choice = self.player_choices()
            print("Press Enter when ready to continue....")
            time.sleep(1)
            print(f"\n{player_1_name}, Please look away...! Let {player_2_name} enter...")
            player_2_choice = self.player_choices()
            print("Press Enter when ready to continue....")
            print(f"\n{player_1_name} chose: {player_1_choice}")
            print(f"\n{player_2_name} chose: {player_2_choice}")
            
            result= self.determine_winner_friend(player_1_choice,player_2_choice, player_1_name, player_2_name)
            print(result)
    
            time.sleep(1)
            print("\nCalculating results.....")
            print("================================")
            time.sleep(3)
            
        

            self.save_scores_friend()
            # reading from the score.txt
            print("---------------- SCORES -------------------")
            
            with open("score_friend.txt", "r") as file:
                scores = file.read()
            print(scores)
            
            print(" ------------------------------------------")
              
                 
            
            print(f"Player1_Wins: {self.player1_wins}, Player2_Wins: {self.player2_wins}, Draws: {self.draws}")

            if self.player1_wins > self.player2_wins: 
                print(f"{player_1_name} is on wining streak...!")

            elif self.player2_wins > self.player1_wins:
                print(f"{player_2_name} is on wining streak...!")

            else:
                emoji = "\U0001F923"
                print("Its neck and neck! Keep playing to see who comes out on top.", emoji)
            
            
            print("---------------------------------------------")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            
            if play_again != "yes":
                print("Thanks for playing, COME BACK AGAIN")
                print("------------------------------------------")

                break

class Game_Setup(Main1, Main2):
    def __init__(self):
        self.wins=0
        self.losses=0
        self.ties=0
        self.player1_wins=0
        self.player2_wins=0
        self.draws=0
        self.choices = ["rock", "paper", "scissors"]

    def Play_game_setup(self):
        # while loops
        while True:
            print("\n")
            print("===========================================================")
            print("=                                                         =")
            print("=      WELCOME TO ROCK, PAPER AND SCISSORS GAME           =")
            print("=                                                         =")
            print("===========================================================")
            print("SELECT ONE OPTION")
            print("-------------------------------")
            print("A. Play against the computer")
            print("B. Play with a friend")
            print("C. Exit the game")
            print("\n")
            choice = input("Enter your Choice (A, B, C): ")
            # decison making
            if choice == "A" or choice == "a":
                self.play_with_computer()
            elif choice == "B" or choice == "b":
                self.play_with_friend()
            elif choice == "C" or choice == "c":
                print("-------------------------------")
                print("Thanks for visiting our developing game")
                break
            else:
                print("Invalid Choice, pick from (A, B, C)")

if __name__ == "__main__":
    game = Game_Setup()
    game.Play_game_setup()
    
