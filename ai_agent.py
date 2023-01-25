from borad import TicTacToeBoard
from copy import deepcopy
from time import sleep

class IntelligentOpponent:
    class State:
        def __init__(self, board: TicTacToeBoard, turn):
            self.board = board
            self.terminal = None
            self.turn = turn

        def printState(self):
            print()
            print("###")
            self.board.printBoard()
            print("isTerminal:", self.isTerminal())
            print(self.turn)
            print("###")
            print()
            

        def nextTurn(self):
            if self.turn == "X":
                return "O"
            else:
                return "X"

        def isTerminal(self):
            if self.terminal == None:
                for i in range(3):
                    if self.board.board[i][0] == self.board.board[i][1] and self.board.board[i][1] == self.board.board[i][2] and self.board.board[i][1] != None:
                        self.terminal = True
                        return True

                for j in range(3):
                    if self.board.board[0][j] == self.board.board[1][j] and self.board.board[1][j] == self.board.board[2][j] and self.board.board[1][j] != None:
                        self.terminal = True
                        return True

                if self.board.board[0][0] == self.board.board[1][1] and self.board.board[1][1] == self.board.board[2][2] and self.board.board[1][1] != None:
                    self.terminal = True
                    return True

                if self.board.board[0][2] == self.board.board[1][1] and self.board.board[1][1] == self.board.board[2][0] and self.board.board[1][1] != None:
                    self.terminal = True
                    return True

                empty_count = 0

                for i in range(3):
                    for j in range(3):
                        if self.board.board[i][j] == None:
                            empty_count += 1
                if empty_count == 0:
                    self.terminal = True
                    return True

                self.terminal = False
                return False
            else:
                return self.terminal

        def make_next_state(self, i, j):
            s = deepcopy(self)
            if s.board.board[i][j] == None:
                s.board.board[i][j] = self.turn
                s.turn = self.nextTurn()
                s.terminal = None
                return s
            else:
                return None

        def expand(self):
            expanded_states = []
            for i in range(3):
                for j in range(3):
                    next = self.make_next_state(i, j)
                    if next != None:
                        expanded_states.append(next)
                        # next.printState()
                        # sleep(1)

            return expanded_states

        def value(self):
            if self.isTerminal():
                for i in range(3):
                    if self.board.board[i][0] == self.board.board[i][1] and self.board.board[i][1] == self.board.board[i][2] and self.board.board[i][1] != None:
                        if self.board.board[i][1] == "X":
                            return 1
                        else:
                            return -1

                for j in range(3):
                    if self.board.board[0][j] == self.board.board[1][j] and self.board.board[1][j] == self.board.board[2][j] and self.board.board[1][j] != None:
                        if self.board.board[1][j] == "X":
                            return 1
                        else:
                            return -1

                if self.board.board[0][0] == self.board.board[1][1] and self.board.board[1][1] == self.board.board[2][2] and self.board.board[1][1] != None:
                    if self.board.board[1][1] == "X":
                        return 1
                    else:
                        return -1

                if self.board.board[0][2] == self.board.board[1][1] and self.board.board[1][1] == self.board.board[2][0] and self.board.board[1][1] != None:
                    if self.board.board[1][1] == "X":
                        return 1
                    else:
                        return -1

                empty_count = 0

                for i in range(3):
                    for j in range(3):
                        if self.board.board[i][j] == None:
                            empty_count += 1
                if empty_count == 0:
                    return 0

                return 0
            else:
                if self.turn == "O":
                    return self.min_value()
                elif self.turn == "X":
                    return self.max_value()

        def min_value(self):
            min = +5
            for s in self.expand():
                v = s.value()
                if v < min:
                    min = v
            return min

        def max_value(self):
            max = -5
            for s in self.expand():
                v = s.value()
                if v > max:
                    max = v
            return max

    def __init__(self, board):
        self.board = board
        print("Hi! I'm your intelligent opponent. Are you ready to be defeated?! Ha Ha ...")

    def takeTurn(self):
        currentState = self.State(self.board, "X")
        expanded_states = currentState.expand()
        max_value = currentState.value()
        print("So I think the game will go: " , max_value)
        for i in expanded_states:
            if i.value() == max_value:
                self.board = i.board
                # print()
                # self.board.printBoard()
        return (max_value, self.board.board)
