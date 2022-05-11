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
    try:
        x, y = int(x), int(y)
        board.board[x][y] in board.board

    except IndexError:
        print(f"Invalid entry: row and column must be an integer between 0 - {board.size - 1}.\n")
        return False

    except ValueError:
        print(f"Invalid entry: Sorry, you can only enter integer numbers.\n")
        return False

    except Exception as e:
        print(f"Invalid entry: {e}\n")
        return False
    else:
        if (x, y) in board.guesses:
            print("You cannot guess the same coordinates twice!\n")
            return False
    return True

def populate_board(board):
    x = random_point(board.size)
    y = random_point(board.size)
    board.add_ship(x, y)

def make_guess(board):
    while True:
        if board.type == "computer":
            x, y = random_point(board.size), random_point(board.size)
            if validate_coordinates(x, y, board):
                board.guesses.append((x, y))
                return x, y
                break
            
                
        elif board.type == "player":
            x = input("Guess a row: ")
            y = input("Guess a column: ")                      
            if validate_coordinates(x, y, board): 
                board.guesses.append((x, y))
                return x, y                
                break

def play_game(computer_board, player_board):
    pass

def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the 
    scores and initialises the boards.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to the ULTIMATE BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of Ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input('Please input your name:\n')

    computer_board = Board(size, num_ships, "Computer", type="computer") 
    player_board = Board(size, num_ships, player_name, type="player") 

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    print("-" * 35)
    print_board(computer_board, player_board)
    play_game(computer_board, player_board)   

