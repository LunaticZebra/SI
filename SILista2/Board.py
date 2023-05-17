import copy


class Board:
    board = []

    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 1
        self.board[3][4] = self.board[4][3] = 2
        self.current_player = 1

    def is_valid_direction(self, row, col, row_direction, col_direction, player):
        opponent = 3 - player
        curr_row = row + row_direction
        curr_col = col + col_direction
        if curr_row < 0 or curr_row >= 8 or curr_col < 0 or curr_col >= 8:
            return False
        if self.board[curr_row][curr_col] != opponent:
            return False
        while 0 <= curr_row < 8 and 0 <= curr_col < 8:
            curr_piece = self.board[curr_row][curr_col]
            if curr_piece == 0:
                return False
            if curr_piece == self.current_player:
                return True
            curr_row += row_direction
            curr_col += col_direction
        return False

    def check_if_valid_move(self, row, col, player):
        if self.board[row][col] != 0:
            return False
        for row_direction in range(-1, 2):
            for col_direction in range(-1, 2):
                if row_direction != 0 or col_direction != 0:
                    if self.is_valid_direction(row, col, row_direction, col_direction, player):
                        return True
        return False

    def get_valid_moves(self, player):
        moves = set()
        for row in range(8):
            for col in range(8):
                if self.check_if_valid_move(row, col, player):
                    moves.add((row, col))
        return moves


    def make_move(self, row, col):

        self.board[row][col] = self.current_player
        for row_direction in range(-1, 2):
            for col_direction in range(-1, 2):
                if row_direction == 0 and col_direction == 0:
                    continue
                if self.is_valid_direction(row, col, row_direction, col_direction, self.current_player):
                    self.change_colour(row, col, row_direction, col_direction)
        self.current_player = 3 - self.current_player
    def change_colour(self, row, col, row_direction, col_direction):
        curr_row = row + row_direction
        curr_col = col + col_direction
        while self.board[curr_row][curr_col] != self.current_player:
            self.board[curr_row][curr_col] = self.current_player
            curr_row += row_direction
            curr_col += col_direction

    def count_points(self):
        points = [0, 0, 0]
        for row in range(8):
            for col in range(8):
                points[self.board[row][col]] += 1
        return points

    def get_winner(self):
        points = self.count_points()
        if points[1] > points[2]:
            return 1
        elif points[2] > points[1]:
            return 2
        else:
            return 0

    def print_board(self):
        for row in self.board:
            row_to_print = ""
            for element in row:
                row_to_print += str(element) + " "
            print(row_to_print)

    def count_corners(self):
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        corner_count = [0, 0]
        for row, col in corners:
            corner = self.board[row][col]
            if corner == 1:
                corner_count[0] += 1
            elif corner == 2:
                corner_count[1] += 1
        return corner_count

    def count_edges(self):
        edges_count = [0, 0]
        for row in range(8):
            left_edge = self.board[row][0]
            right_edge = self.board[row][7]
            if left_edge == 1:
                edges_count[0] += 1
            elif left_edge == 2:
                edges_count[1] += 1
            if right_edge == 1:
                edges_count[0] += 1
            elif right_edge == 2:
                edges_count[1] += 1
        return edges_count

    def get_board(self):
        return self.board

    def copy(self):
        new_board = Board()
        new_board.board = copy.deepcopy(self.board)
        new_board.current_player = self.current_player
        return new_board


def main():
    game = Board()
    game.copy()
    counter = 0
    while True:
        valid_moves = game.get_valid_moves(game.current_player)
        if not valid_moves:
            counter += 1
            if counter == 2:
                break
            else:
                print("No valid moves")
                game.current_player = 3 - game.current_player
                continue
        counter = 0
        print(f"Player {game.current_player}'s turn")
        game.print_board()
        print(f"Valid moves: {valid_moves}")
        row, col = map(int, input("Enter row and column: ").split())
        if (row, col) in valid_moves:
            game.make_move(row, col)
        else:
            print("Invalid move")
            game.current_player = 3 - game.current_player
        print(game.count_points())

    game.print_board()
    winner = game.get_winner()
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

