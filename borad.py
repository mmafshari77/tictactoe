class TicTacToeBoard:

    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def printBoard(self):
        for row in self.board:
            self.printRow(row)

    def printRow(self, row):
        to_be_printed = []
        for r in row:
            if r == None:
                to_be_printed.append("-")
            else:
                to_be_printed.append(r)
        print(" ".join(to_be_printed))

    def getBoard():
        return self.board

    def checkWhoIsWinner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][1] != None:
                return self.board[i][0]

        for j in range(3):
            if self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j] and self.board[1][j] != None:
                return self.board[0][j]

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[1][1] != None:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[1][1] != None:
            return self.board[0][2]
