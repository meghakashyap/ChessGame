# importing  chess library
import chess

# creating board using chess.Board()
board = chess.Board()

# Defining the moves which we can use while playing game
Move = board.legal_moves

print("Its a legal moves")
print(Move)
print(board)

# Runing  loop for game
while True:
    # asking user to move
    user = input("Enter your move using legal moves ex- e4,e5 or for stoping the game press  s or S\n:-")
        
    # making move of players using push_san() 
    board.push_san(user)
    print(board)
    print(Move)
    
    #  Verifying check mate
    board.is_checkmate()

    # Verifying stalemate
    board.is_stalemate()

    # code
    board.is_check()

    # code
    board.is_fivefold_repetition()
    board.is_seventyfive_moves()

print(board)
