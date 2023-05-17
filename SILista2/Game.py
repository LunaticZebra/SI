from Algorithms import *
import numpy as np

def make_minimax_move(board, heuristic, depth, curr_player):
    return minimax(True, board, depth, heuristic, curr_player)


def make_alpha_beta_move(board, heuristic, depth, curr_player):
    return alpha_beta_cut(True, board, depth, heuristic, -math.inf, math.inf, curr_player)


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
            _, best_node = algorithm1(game_board, heuristic1, depth, 1)
            player1_time += time.time() - move_start
            player1_moves_performed += 1
        elif game_board.current_player == 2:
            move_start = time.time()
            _, best_node = algorithm2(game_board, heuristic2, depth, 2)
            player2_time += time.time() - move_start
            player2_moves_performed += 1
        if game_board != best_node:
            game_board = best_node
        else:
            row, col = list(valid_moves)[0]
            game_board.make_move(row, col)

    winner = game_board.get_winner()
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

    print(game_board.count_points())
    return player1_moves_performed, player1_time, player2_moves_performed, player2_time

start_time = time.time()
moves1, time1, moves2, time2 = game(make_minimax_move, Heuristics.simple_count, make_minimax_move, Heuristics.reverse_best_movability, 4)
game_time = time.time() - start_time
print(f"Game time = {game_time} seconds")
print(f"Player1 time per move = {time1/moves1} seconds")
print(f"Player1 moves= {moves1} ")
print(f"Player2 time per move = {time2/moves2} seconds")
print(f"Player2 moves = {moves2}")

