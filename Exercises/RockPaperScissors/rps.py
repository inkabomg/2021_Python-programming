from player import HumanPlayer, CPUPlayer
import random

class RockPaperScissors():

    def __init__(self, human=True):
        self.human = human
        self.player = self.create_player()
        self.computer = 'Dumb computer'
        self.winner = None

    def create_player(self):
        if self.human:
            # Asking for player's name
            name = input("Please enter your name: ")
            return name

    def run_game(self):
        while self.winner is None:
            user = HumanPlayer()
            comp = CPUPlayer()
            # Call player_hand method to get the player's hand.
            human_input = user.player_hand()
            # Call computer_hand method to get the computer's hand.
            cpu_hand = comp.computer_hand()
            self.display_choices(human_input, cpu_hand)

            if human_input == cpu_hand:
                print ("It's a tie!")
                self.run_game()
            elif human_input == 'rock' and cpu_hand == 'scissor':
                self.winner = self.player
                self.display_winner(self.winner)
            elif human_input == 'paper' and cpu_hand == 'scissor':
                self.winner = self.computer
                self.display_winner(self.winner)
            elif human_input == 'rock' and cpu_hand == 'paper':
                self.winner = self.computer
                self.display_winner(self.winner)
            elif human_input == 'scissor' and cpu_hand == 'paper':
                self.winner = self.player
                self.display_winner(self.winner)
            elif human_input == 'paper' and cpu_hand == 'rock':
                self.winner = self.player
                self.display_winner(self.winner)
            elif human_input == 'scissor' and cpu_hand == 'rock':
                self.winner = self.computer
                self.display_winner(self.winner)

    def display_choices(self, human_input, cpu_hand):
        print ("{}: {}".format(self.player, human_input))
        print ("{}: {}".format(self.computer, cpu_hand))

    def display_winner(self, winner):
        print ("{} wins!".format(self.winner))

if __name__ == "__main__":
    while True:
        game = RockPaperScissors()
        game.run_game()

        while True:
            continue_prompt = input('\nDo you wish to play again? (y/n): ').lower()
            if continue_prompt == 'n':
                print("The end.")
                exit()
            elif continue_prompt == 'y':
                break
            else:
                print("Invalid input!\n")
                continue