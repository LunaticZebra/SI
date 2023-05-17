import math
import timeit

import Heuristics
from Board import Board
from Node import Node


def generate_decision_tree(board, initial_depth):
    root = Node(board)
    def rec_generate(node, depth):
        if depth == 0:
            return None
        moves = node.data.get_valid_moves(node.data.current_player)
        for row, col in moves:
            board_copy = node.data.copy()
            board_copy.make_move(row, col)
            child = Node(board_copy)
            child.parent = (row, col)
            node.children.append(child)
            rec_generate(child, depth - 1)

    rec_generate(root, initial_depth)
    return root


def minimax(maximising_player, node, depth, heuristic):
    best_node = node
    if depth == 0:
        return heuristic(node.data), node
    elif maximising_player:
        best_val = -math.inf
        for child in node.children:
            child_val, _ = minimax(False, child, depth - 1, heuristic)
            if child_val > best_val:
                best_val = child_val
                best_node = child
    else:
        best_val = math.inf

        for child in node.children:
            child_val, _ = minimax(True, child, depth - 1, heuristic)
            if child_val < best_val:
                best_val = child_val
                best_node = child

    return best_val, best_node


def alpha_beta_cut(maximising_player, node, depth, heuristic, alpha, beta):
    best_node = node
    if depth == 0:
        return heuristic(node.data), node
    elif maximising_player:
        best_val = alpha

        for child in node.children:
            child_val, _ = alpha_beta_cut(False, child, depth - 1, heuristic, best_val, beta)
            if child_val > best_val:
                best_val = child_val
                best_node = child
                if beta <= best_val:
                    break
    else:
        best_val = beta

        for child in node.children:
            child_val, _ = alpha_beta_cut(True, child, depth - 1, heuristic, alpha, best_val)
            if child_val < best_val:
                best_val = child_val
                best_node = child
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
    root = Board()
    depth = 6
    tree_root = generate_decision_tree(root, depth)
    print(count_nodes(tree_root))
    execution_time_tree_generation = timeit.timeit(lambda: generate_decision_tree(root, depth), number=1)
    execution_time_minimax = timeit.timeit(lambda: minimax(True, tree_root, depth, Heuristics.least_opponent_moves), number=1)
    score2, score_node2 = minimax(True, tree_root, depth, Heuristics.least_opponent_moves)
    score, score_node = alpha_beta_cut(True, tree_root, depth, Heuristics.least_opponent_moves, -math.inf, math.inf)
    execution_time_alpha_beta = timeit.timeit(lambda: alpha_beta_cut(True, tree_root, depth, Heuristics.least_opponent_moves, -math.inf, math.inf), number=1)
    print(execution_time_tree_generation)
    print(execution_time_minimax)
    print(execution_time_alpha_beta)
    print(score)
    score_node.data.print_board()
    print(score2)
    score_node2.data.print_board()
    print(score_node2.parent)
