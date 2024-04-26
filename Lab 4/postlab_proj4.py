import random
import oxo_data


class Game:
    def __init__(self):
        self.board = list(" " * 9)

    def save(self):
        oxo_data.saveGame(self.board)

    def restore(self):
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
            else:
                self.board = list(" " * 9)
        except IOError:
            self.board = list(" " * 9)

    def _generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self, player):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == player * 3:
                return True
        return False

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self._is_winning_move('X'):
            return 'X'
        else:
            return ""

    def computer_move(self):
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._is_winning_move('O'):
            return 'O'
        else:
            return ""

    def play(self):
        result = ""
        while not result:
            print(self.board)
            try:
                result = self.user_move(self._generate_move())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()
            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(self.board)


if __name__ == "__main__":
    game = Game()
    game.play()