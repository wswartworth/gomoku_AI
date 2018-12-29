import tkinter as tk
import gamestate
import minimax
import board
import sys

#improvement: transpositions
#improvement: having more stones on the board gives a score advantage
#not fair if you sometimes play deeper (or if the depth differs in parity)

size = 12
depth_1 = 2
depth_2 = 2

gamestate = gamestate.GameState(size, size, 5)

def sim_game():
    AI_1 = minimax.Minimax(gamestate, 1, depth_1, random_range=0.01)
    AI_2 = minimax.Minimax(gamestate, -1, depth_2, random_range=0.01)

    turn = 1

    while(not AI_1.gamestate.gameOver()):

       if(turn == 1):
            move = AI_1.getAIMove()
       else:
            move = AI_2.getAIMove()
       AI_1.makeMove(move)
       AI_2.makeMove(move)
       turn = (-1)*turn
    winner = AI_1.gamestate.winner
    return winner;

stats = [0,0,0]
for i in range(0,100):
    winner = sim_game()
    stats[winner+1] += 1
    print(stats)

top = tk.Tk()
gameboard = board.Board(top,AI_1.gamestate,None, None)
top.mainloop()

    
