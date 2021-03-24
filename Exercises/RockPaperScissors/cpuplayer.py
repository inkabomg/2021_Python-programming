from player import Player
import random

class CPUPlayer(Player):
    def __init__(self):
        self.hand = []
    
    def computer_hand(self):
        computer_input = random.randint(1,3)
        if computer_input == 1:
            return 'rock'
        elif computer_input == 2:
            return 'paper'
        elif computer_input == 3:
            return 'scissor'