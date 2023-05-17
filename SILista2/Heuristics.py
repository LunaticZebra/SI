PLAYER_1 = 1
PLAYER_2 = 2
EDGE_WEIGHT = 2
CORNER_WEIGHT = 10
POINTS_MAP = [
    [8, 1, 5, 5, 5, 5, 1, 8],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [5, 1, 3, 3, 3, 3, 1, 5],
    [5, 1, 3, 0, 0, 3, 1, 5],
    [5, 1, 3, 0, 0, 3, 1, 5],
    [5, 1, 3, 3, 3, 3, 1, 5],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [8, 1, 5, 5, 5, 5, 1, 8],
]


def take_corners(board):
    points = board.count_points()
    player1_points = points[1]
    player2_points = points[2]
    player1_corner, player2_corner = board.count_corners()

    return player1_points - player2_points + (player1_corner - player2_corner) * (CORNER_WEIGHT - 1)


def reverse_take_corners(board):
    points = board.count_points()
    player1_points = points[1]
    player2_points = points[2]
    player1_corner, player2_corner = board.count_corners()

    return player2_points - player1_points + (player2_corner - player1_corner) * (CORNER_WEIGHT - 1)


def take_edges(board):
    player1_edges, player2_edges = board.count_edges()
    points = board.count_points()
    player1_points = points[1]
    player2_points = points[2]
    return (player1_edges - player2_edges) * (EDGE_WEIGHT - 1) + player1_points - player2_points


def reverse_take_edges(board):
    player1_edges, player2_edges = board.count_edges()
    points = board.count_points()
    player1_points = points[1]
    player2_points = points[2]
    return (player2_edges - player1_edges) * (EDGE_WEIGHT - 1) + player2_points - player1_points


def simple_count(board):
    players_points = board.count_points()
    return players_points[0] - players_points[1]


def reverse_simple_count(board):
    players_points = board.count_points()
    return players_points[1] - players_points[2]


def best_movability(board):
    return len(board.get_valid_moves(PLAYER_1)) - len(board.get_valid_moves(PLAYER_2))


def reverse_best_movability(board):
    return len(board.get_valid_moves(PLAYER_2)) - len(board.get_valid_moves(PLAYER_1))


def least_opponent_moves(board):
    return -len(board.get_valid_moves(PLAYER_2))


def reverse_least_opponent_moves(board):
    return -len(board.get_valid_moves(PLAYER_1))


def points_map(board):
    points_board = board.get_board()
    player1_points = 0
    player2_points = 0
    for row in range(8):
        for col in range(8):
            point = points_board[row][col]
            if point == 1:
                player1_points += POINTS_MAP[row][col]
            elif point == 2:
                player2_points += POINTS_MAP[row][col]
    return player1_points - player2_points


def reverse_points_map(board):
    points_board = board.get_board()
    player1_points = 0
    player2_points = 0
    for row in range(8):
        for col in range(8):
            point = points_board[row][col]
            if point == 1:
                player1_points += POINTS_MAP[row][col]
            elif point == 2:
                player2_points += POINTS_MAP[row][col]
    return player2_points - player1_points
