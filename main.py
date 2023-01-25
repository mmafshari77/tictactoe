from ai_agent import IntelligentOpponent
from borad import TicTacToeBoard
from random import randint

board = TicTacToeBoard()
intlOpp = IntelligentOpponent(board)
print("The game is about to be started!")
print()

while True:
    winner = board.checkWhoIsWinner()
    if winner != None:
        print()
        print("And the winner is ", winner)
        break

    i = input("Enter the x-position you want to put O: ")
    j = input("Enter the y-position you want to put O: ")

    board.board[int(i)][int(j)] = "O"

    board.printBoard()
    ai_res = intlOpp.takeTurn()
    print("Estimate from your opponent:", ai_res[0])
    board.board = ai_res[1]
    board.printBoard()

    


