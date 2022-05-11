from random import randint

scores = {'computer': 0, 'player': 0}

# Board class adopted and modified from the CI's battleship tutorial
class Board:
    """
    Main board class. Sets board size, the number of ships,
     the player's name and the board type (player board or computer).
     Has methods for adding ships and guesses and printing the board
     """


    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type  = type
        self.guesses = []
        self.ships = []


    def print(self):
        # prints board
        for row in self.board:
            print("  ".join(row))

    def guess(self, x, y):
        # appends X at the chosen coordinates
        self.board[x][y] = "X"

        # appends * if chosen coordinates hits a target
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def random_point(size):
    """
    Helper function to return a random integer between o and size
    """
    return randint(0, size - 1)

def validate_coordinates(x, y, board):
    pass

def populate_board(board):
    pass

def make_guess(board):
    pass

def play_game(computer_board, player_board):
    pass

def new_game():
   pass  

