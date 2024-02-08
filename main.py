import os
from board import Board
from random import choice



def take_input(free):
    spot = int(input(f"In which spot to do want to place your mark? {free}\n"))
    return spot



def main():
    os.system('clear')
    board=Board()
    print (board)
    p1="X"
    p2="O"
    turn=choice([p1,p2])
    sym=0

    while not board.game_over:
        print (f"It is {turn} to play.")

        if len(board.free_spots)==0:
            print ("No more fields to mark, its a draw")
            board.game_over=True
            break
        if sym in board.free_spots:
            board.mark(spot=int(sym-1),player=turn)
            if turn == p1:
                turn = p2
            else:
                turn = p1
        else:
            sym=take_input(board.free_spots)



if __name__ == "__main__":
    main()