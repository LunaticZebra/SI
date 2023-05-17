import time

import Heuristics
from Algorithms import *


def make_minimax_move(board, heuristic, depth):
    root = generate_decision_tree(board, depth)
   # print(count_nodes(root))
    return minimax(True, root, depth, heuristic)


def make_alpha_beta_move(board, heuristic, depth):
    root = generate_decision_tree(board, depth)
   # print(count_nodes(root))
    return alpha_beta_cut(True, root, depth, heuristic, -math.inf, math.inf)


def game(algorithm1, heuristic1, algorithm2, heuristic2, depth):
    game_board = Board()
    counter = 0
    player1_moves_performed = 0
    player2_moves_performed = 0
    player1_time = 0
    player2_time = 0
    while True:
        valid_moves = game_board.get_valid_moves(game_board.current_player)
        if not valid_moves:
            counter += 1
            if counter == 2:
                break
            else:
                #print("No valid moves")
                game_board.current_player = 3 - game_board.current_player
                continue
        counter = 0
        #print(f"Player {game_board.current_player}'s turn")
        #game_board.print_board()
        #print(f"Valid moves: {valid_moves}")

        if game_board.current_player == 1:
            move_start = time.time()
            _, best_node = algorithm1(game_board, heuristic1, depth)
            player1_time += time.time() - move_start
            player1_moves_performed += 1
        elif game_board.current_player == 2:
            move_start = time.time()
            _, best_node = algorithm2(game_board, heuristic2, depth)
            player2_time += time.time() - move_start
            player2_moves_performed += 1
        if best_node.parent == None:
            row, col = list(valid_moves)[0]
        else:
            row, col = best_node.parent
        if (row, col) in valid_moves:
            game_board.make_move(row, col)
        else:
           # print("Invalid move")
            game_board.current_player = 3 - game_board.current_player
       # print(game_board.count_points())

    game_board.print_board()
    winner = game_board.get_winner()
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

    print(game_board.count_points())
    return player1_moves_performed, player1_time, player2_moves_performed, player2_time

start_time = time.time()
moves1, time1, moves2, time2 = game(make_minimax_move, Heuristics.simple_count, make_minimax_move, Heuristics.reverse_best_movability, 6)
game_time = time.time() - start_time
print(f"Game time = {game_time} seconds")
print(f"Player1 time per move = {time1/moves1} seconds")
print(f"Player1 moves= {moves1} ")
print(f"Player2 time per move = {time2/moves2} seconds")
print(f"Player2 moves = {moves2}")

