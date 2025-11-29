import random

class rockPaperScissorsGame:
    """
    Rock Paper Scissors game class with OOP structure.

    Attributes:
        player_score (int): Player's current score.
        computer_score (int): Computer's current score.
        valid_choices (list): List of valid inputs.
    """

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.valid_choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        """
        Randomly select a choice for the computer.

        Returns:
            str: Computer's choice (rock/paper/scissors)
        """
        computer_choice = random.choice(self.valid_choices)
        return computer_choice
    
    def get_player_choice(self):
        """
        Get input from player via CLI. Ensures valid input.

        Returns:
            str: Player's choice (rock/paper/scissors)
        """
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in self.valid_choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            return self.get_player_choice()
        return player_choice

    def specify_winner(self, player_choice, computer_choice):
        """
        Determine winner of a single round and update scores.

        Args:
            player_choice (str): Player's selection.
            computer_choice (str): Computer's selection.

        Returns:
            str: Result message ("Player wins!", "Computer wins!", "It's a tie!")
        """
        player_win_situations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice, computer_choice) in player_win_situations:
            self.player_score += 1
            return "Player wins!"
        else:
            self.computer_score += 1
            return "Computer wins!"
        
    def play(self):
        """
        Play a single round of Rock Paper Scissors using CLI.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        result = self.specify_winner(player_choice, computer_choice)
        print(f"Player chose: {player_choice} \t Computer chose: {computer_choice}")
        print(result)
        print(f"Player score: {self.player_score} \t Computer score: {self.computer_score}")


def main():
    """
    Entry point for CLI version. 
    Game continues until either player or computer reaches score of 3.
    """
    while True:
        game = rockPaperScissorsGame()
        while True:
            game.play()
            if game.player_score >= 3:
                print("Player wins the game!")
                break
            elif game.computer_score >= 3:
                print("Computer wins the game!")
                break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break
                

if __name__ == "__main__":
    main()
