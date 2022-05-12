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
        self.type = type
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
        print("Invalid data: row and column must be an integer between 0 - 4.")
        return False

    except ValueError:
        print(f"Invalid data: sorry, you can only enter integer numbers.\n")
        return False

    except Exception as e:
        print(f"Invalid data: {e}\n")
        return False
    finally:
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


def scores_dashboard(board):
    """
    Prints the score dashboard status after each round
    """
    print("-" * 35)
    print("After this round, the scores are:")
    print(f"{board.name}: {scores['player']} Computer: {scores['computer']}")
    print("-" * 35)


def print_board(computer_board, player_board):
    """
    Prints the player's board and the computer's board
    """
    print(f"{player_board.name}'s Board:")
    player_board.print()
    print()
    print("Computer's Board:")
    computer_board.print()
    print("-" * 35)


def check_winner(scores, computer_board, player_board):
    """
    Checks winner and displays winning message
    """
    if (scores['player'] == player_board.num_ships and
       scores['computer'] == player_board.num_ships):
            print("GAME OVER!!\n You both have a tie!")
    elif scores["player"] == player_board.num_ships:
        print("GAME OVER!!")
        print(f"Well done {player_board.name}!! You are the Victor")
    elif scores['computer'] == player_board.num_ships:
        print("GAME OVER!!")
        print(f"Sorry, {player_board.name}!! You lost to the computer")


def play_game(computer_board, player_board):
    """
    Main game function. Takes in the board instances as arguement
    and controls the game logic"""
    while True:
        # Get the player's guess and populate computer's board
        x, y = make_guess(player_board)
        x, y = int(x), int(y)
        player_board.guesses.append((x, y))
        print(f"Player guessed: {x, y}")
        if computer_board.guess(x, y) == "Hit":
            print("Player got a hit!")
            scores['player'] += 1
        elif computer_board.guess(x, y) == "Miss":
            print("Player missed this time")

        # Get computer's guess and populate player's board
        x, y = make_guess(computer_board)
        computer_board.guesses.append((x, y))
        print(f"Computer guessed: {x, y}")
        if player_board.guess(int(x), int(y)) == "Hit":
            print("Computer got a hit!")
            scores["computer"] += 1
        elif player_board.guess(x, y) == "Miss":
            print("Computer missed this time")

        scores_dashboard(player_board)
        print_board(computer_board, player_board)
        check_winner(scores, computer_board, player_board)

        # Get user's feedback to quit or to continue
        player_choice = input("Enter 'e' to quit, 'n' for new game and \
any key to continue: ")

        if player_choice.lower() == "n":
            new_game()
        elif player_choice.lower() == "e":
            break


def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the boards.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 37)
    print("Welcome to the ULTIMATE BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of Ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 37)
    player_name = input('Please input your name:\n')
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    print("-" * 35)
    print_board(computer_board, player_board)
    play_game(computer_board, player_board)


new_game()
