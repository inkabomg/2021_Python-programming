from player import Player

class HumanPlayer(Player):
    def __init__(self):
        self.hand = []

    def player_hand(self):
        player_input = input('Choose r = rock, p = paper or s = scissor: ')
        if player_input not in 'rpsRPS':
            print ('Invalid input. Please try again.')
            self.player_hand()
        elif player_input == 'r' or player_input == 'R':
            player_input = 'rock'
            return player_input
        elif player_input == 'p' or player_input == 'P':
            player_input = 'paper'
            return player_input
        elif player_input == 's' or player_input == 'S':
            player_input = 'scissor'
            return player_input