import math
import random


class Player:

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        val = None

        while not valid_spot:
            spot = input(f"{self.letter} turn. Choose spot(1-9): ")

            if spot == 'Q' or spot == 'q':
                quit()

            try:
                spot = int(spot)
                val = game.board_mapping.get(spot)

                if val not in game.available_moves():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid spot. Try Again.')

        return val
