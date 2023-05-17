import math
import timeit
import time
import Heuristics
from Board import Board
from Node import Node


def minimax(maximising_player, board: Board, depth, heuristic, curr_player):
    best_node = board
    if depth == 0:
        return heuristic(board), board
    elif maximising_player:
        best_val = -math.inf
        for row, col in board.get_valid_moves(curr_player):
            new_board = board.copy()
            new_board.make_move(row, col)

            child_val, _ = minimax(False, new_board, depth - 1, heuristic, curr_player)
            if child_val > best_val:
                best_val = child_val
                best_node = new_board
    else:
        best_val = math.inf

        for row, col in board.get_valid_moves(curr_player):
            new_board = board.copy()
            new_board.make_move(row, col)

            child_val, _ = minimax(True, new_board, depth - 1, heuristic, curr_player)
            if child_val < best_val:
                best_val = child_val
                best_node = new_board

    return best_val, best_node


def alpha_beta_cut(maximising_player, board: Board, depth, heuristic, alpha, beta, curr_player):
    best_node = board
    if depth == 0:
        return heuristic(board), board
    elif maximising_player:
        best_val = alpha

        for row, col in board.get_valid_moves(curr_player):
            new_board = board.copy()
            new_board.make_move(row, col)

            child_val, _ = alpha_beta_cut(False, new_board, depth - 1, heuristic, best_val, beta, curr_player)
            if child_val > best_val:
                best_val = child_val
                best_node = new_board
                if beta <= best_val:
                    break
    else:
        best_val = beta

        for row, col in board.get_valid_moves(curr_player):
            new_board = board.copy()
            new_board.make_move(row, col)

            child_val, _ = alpha_beta_cut(True, new_board, depth - 1, heuristic, alpha, best_val, curr_player)
            if child_val < best_val:
                best_val = child_val
                best_node = new_board
                if alpha >= best_val:
                    break

    return best_val, best_node


def count_nodes(root):
    if root is None:
        return 0

    count = 1
    for child in root.children:
        count += count_nodes(child)

    return count


if __name__ == '__main__':
    board = Board()
    depth = 5
    start_time = time.time()
    _, node_minimax = minimax(True, board, depth, Heuristics.simple_count)
    print(time.time() - start_time)
    start_time = time.time()
    _, node_alphabeta = alpha_beta_cut(True, board, depth, Heuristics.simple_count, -math.inf, math.inf)
    print(time.time() - start_time)
