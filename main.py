import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QGridLayout, QPushButton, QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignal, QTimer, QThread


class board(QWidget):
    ROWS = 3
    COLLUMNS = 3
    def __init__(self):
        super(board, self).__init__()
        self.setWindowTitle('Tic Tac Toe')
        self.setFixedSize(300,300)
        self.positions = [[0 for i in range(self.ROWS)] for _ in range(self.COLLUMNS)]
        self.create_grid()
        self.turns = {'X': 'O', 'O':'X'}
        self.player = 'X'

    def create_grid(self):
        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.gridLayout.setSpacing(0)
        

        for row, l in enumerate(self.positions):
            for collumn, _ in enumerate(l):
                button = infoButton(row, collumn)
                button.position.connect(self.on_click)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.gridLayout.addWidget(button, row, collumn)
    
    def on_click(self, position):
        row, column = position 
        if self.positions[row][column] != 0:
            print('Illegal move')
        else:
            self.positions[row][column] = self.player
            self.check_winner(self.positions, self.player)
            self.player = self.turns[self.player]
            print('\n'.join([str(x) for x in self.positions]))

    def check_winner(self, board, player):
        if board[0][0] == board[0][1] == board[0][2] == player or \
            board[1][0] == board[1][1] == board[1][2] == player or \
            board[2][0] == board[2][1] == board[2][2] == player or \
            board[0][0] == board[1][0] == board[2][0] == player or \
            board[0][1] == board[1][1] == board[2][1] == player or \
            board[0][2] == board[1][2] == board[2][2] == player or \
            board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
            print(f'{player} win')
            self.destroy()
        elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
            print('No one wins') 
            self.destroy()
                



class infoButton(QPushButton):
    position = pyqtSignal(tuple)
    def __init__(self, row, collumn):
        super().__init__()
        self.row = row
        self.collumn = collumn
        self.clicked.connect(self.positioning)

    def positioning(self):
        self.position.emit((self.row, self.collumn))        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = board()
    window.show()
    sys.exit(app.exec_())
    