import time
from player import HumanPlayer, RandomComputerPlayer

O_PLAYER_SYMBOL = 'O'
X_PLAYER_SYMBOL = 'X'
EMPTY_SYMBOL = ' '


class TicTacToe:

    def __init__(self):
        self.board = [[EMPTY_SYMBOL] * 3 for _ in range(3)]
        self.current_winner = None
        self.board_mapping = self.populate_mappings()

    def populate_mappings(self):
        n = len(self.board)
        mapping = {}

        i = 1
        for row in range(n):
            for col in range(n):
                mapping[i] = (row, col)
                i += 1

        return mapping

    def get_spot_rep(self, spot):
        for key, value in self.board_mapping.items():
            if value == spot:
                return key

    def print_board(self):
        n = len(self.board)

        for row in range(n):
            print('| ', end='')
            for col in range(n):
                val = self.board[row][col]
                print(val, end=' | ')
            print()

    def print_positions(self):
        n = len(self.board)

        i = 1
        for row in range(n):
            print('| ', end='')
            for col in range(n):
                print(i, end=' | ')
                self.board_mapping[i] = (row, col)
                i += 1
            print()

    def available_moves(self):
        n = len(self.board)
        moves = []

        for i in range(n):
            for j in range(n):
                if self.board[i][j] == EMPTY_SYMBOL:
                    moves.append((i, j))
        return moves

    def has_empty_spots(self):
        for row in self.board:
            if EMPTY_SYMBOL in row:
                return True

        return False

    def num_empty_spots(self):
        return len(self.available_moves())

    def make_move(self, spot, letter):
        row, col = spot

        if self.board[row][col] == EMPTY_SYMBOL:
            self.board[row][col] = letter

            if self.winner(spot, letter):
                self.current_winner = letter

            return True

        return False

    def get_diagonals(self):
        back, front = [], []
        n = len(self.board)

        i, j = 0, n - 1
        while i < n and j >= 0:
            front.append(self.board[i][i])
            back.append(self.board[i][j])
            i += 1
            j -= 1

        diagonals = [back, front]
        return diagonals

    def winner(self, spot, letter):
        # Check row
        for row in self.board:
            if all(val == letter for val in row):
                return True

        # Check col
        board_in_cols = list(zip(*self.board))
        for row in board_in_cols:
            if all(val == letter for val in row):
                return True

        # Check Diagonals
        diagonals = self.get_diagonals()
        for diagonal in diagonals:
            if all(val == letter for val in diagonal):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_positions()
        print('Press Q to exit!', end='\n\n')

    current_player = O_PLAYER_SYMBOL

    while game.has_empty_spots():
        if current_player == X_PLAYER_SYMBOL:
            spot = o_player.get_move(game)
        else:
            spot = x_player.get_move(game)

        if game.make_move(spot, current_player):
            square = game.get_spot_rep(spot)

            if print_game:
                print(f'{current_player} makes move to spot {square}')
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(f'{current_player} WINS!!!!')
                return

            # Alternate letters
            X = X_PLAYER_SYMBOL
            current_player = O_PLAYER_SYMBOL if current_player == X else X

        time.sleep(.5)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer(X_PLAYER_SYMBOL)
    o_player = RandomComputerPlayer(O_PLAYER_SYMBOL)
    ttt = TicTacToe()
    # ttt.print_positions()
    # print(ttt.board_mapping)
    play(ttt, x_player, o_player, print_game=True)
