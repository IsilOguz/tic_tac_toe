from lib2to3.pygram import pattern_symbols
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

who = 0     # 0 means Player 1 (O letter),   1 means player 2 (X letter)


class TicTacToeGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(TicTacToeGame,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter = 1  
        self.ui.pushButton.clicked.connect(self.move1)
        self.ui.pushButton_2.clicked.connect(self.move2)
        self.ui.pushButton_3.clicked.connect(self.move3)
        self.ui.pushButton_4.clicked.connect(self.move4)
        self.ui.pushButton_5.clicked.connect(self.move5)
        self.ui.pushButton_6.clicked.connect(self.move6)
        self.ui.pushButton_7.clicked.connect(self.move7)
        self.ui.pushButton_8.clicked.connect(self.move8)
        self.ui.pushButton_9.clicked.connect(self.move9)
        self.ui.buttonReset.clicked.connect(self.reset)

    def disableAllButtons(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.pushButton_3.setDisabled(True)
        self.ui.pushButton_4.setDisabled(True)
        self.ui.pushButton_5.setDisabled(True)
        self.ui.pushButton_6.setDisabled(True)
        self.ui.pushButton_7.setDisabled(True)
        self.ui.pushButton_8.setDisabled(True)
        self.ui.pushButton_9.setDisabled(True)
        

    def move1(self):
        board[0][0] = who
        print(board)
        self.ui.pushButton.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton.setDisabled(True)
        self.changePlayer()
        self.control()
        
    
    def move2(self):
        board[0][1] = who
        print(board)
        self.ui.pushButton_2.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_2.setDisabled(True)
        self.changePlayer()
        self.control()
    
    def move3(self):
        board[0][2] = who
        print(board)
        self.ui.pushButton_3.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_3.setDisabled(True)
        self.changePlayer()
        self.control()
      

    def move4(self):
        board[1][0] = who
        print(board)
        self.ui.pushButton_4.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_4.setDisabled(True)
        self.changePlayer()
        self.control()
        
    
    def move5(self):
        board[1][1] = who
        print(board)
        self.ui.pushButton_5.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_5.setDisabled(True)
        self.changePlayer()
        self.control()
    
    def move6(self):
        board[1][2] = who
        print(board)
        self.ui.pushButton_6.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_6.setDisabled(True)
        self.changePlayer()
        self.control()
    
    def move7(self):
        board[2][0] = who
        print(board)
        self.ui.pushButton_7.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_7.setDisabled(True)
        self.changePlayer()
        self.control()
    
    def move8(self):
        board[2][1] = who
        print(board)
        self.ui.pushButton_8.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_8.setDisabled(True)
        self.changePlayer()
        self.control()

    def move9(self):
        board[2][2] = who
        print(board)
        self.ui.pushButton_9.setText("X" if who == 0 else "O")
        self.ui.labelWho.setText("Player 2 | Tick O" if who == 0 else "Player 1 | Tick X")
        self.ui.pushButton_9.setDisabled(True)
        self.changePlayer()
        self.control()



    def control(self):
        if board[0][0] == board[0][1] == board[0][2] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[1][0] == board[1][1] == board[1][2] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[2][0] == board[2][1] == board[2][2] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[0][0] == board[1][0] == board[2][0] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[0][1] == board[1][1] == board[2][1] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[0][2] == board[1][2] == board[2][2] == 1:
            self.disableAllButtons()
            self.ui.labelWho.setText("Player 2 wins")

        elif board[0][0] == board[1][1] == board[2][2] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[0][2] == board[1][1] == board[2][0] == 1:
            self.ui.labelWho.setText("Player 2 wins")
            self.disableAllButtons()

        elif board[0][0] == board[0][1] == board[0][2] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif board[1][0] == board[1][1] == board[1][2] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif board[2][0] == board[2][1] == board[2][2] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif board[0][0] == board[1][0] == board[2][0] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()
        elif board[0][1] == board[1][1] == board[2][1] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif board[0][2] == board[1][2] == board[2][2] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif board[0][0] == board[1][1] == board[2][2] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif board[0][2] == board[1][1] == board[2][0] == 0:
            self.ui.labelWho.setText("Player 1 wins")
            self.disableAllButtons()

        elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
            self.ui.labelWho.setText("It is a tie")
            self.disableAllButtons()

            
    def changePlayer(self):
        global who
        if who == 0:    
            who = 1
        else:
            who = 0
    
    
    def reset(self):
        global board,who
        board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
        ]
        who=0
        self.ui.pushButton.setText("")
        self.ui.pushButton_2.setText("")
        self.ui.pushButton_3.setText("")
        self.ui.pushButton_4.setText("")
        self.ui.pushButton_5.setText("")
        self.ui.pushButton_6.setText("")
        self.ui.pushButton_7.setText("")
        self.ui.pushButton_8.setText("")
        self.ui.pushButton_9.setText("")
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_2.setDisabled(False)
        self.ui.pushButton_3.setDisabled(False)
        self.ui.pushButton_4.setDisabled(False)
        self.ui.pushButton_5.setDisabled(False)
        self.ui.pushButton_6.setDisabled(False)
        self.ui.pushButton_7.setDisabled(False)
        self.ui.pushButton_8.setDisabled(False)
        self.ui.pushButton_9.setDisabled(False)
        self.ui.labelWho.setText("Player 1 | Tick X")

app = QtWidgets.QApplication(sys.argv)
win = TicTacToeGame()
win.show()
sys.exit(app.exec_())










