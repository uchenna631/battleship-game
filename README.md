#   THE ULTIMATE BATTLESHIP

The Ultimate Battleship is a python terminal game which runs on the Code Institute's mock terminal Heroku

Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one square on the board

[Here is the live version of my project](https://the-ultimate-battleship.herokuapp.com/)



## How to play
Battleship is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet. You can read more about it on [wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version, the player enter's their name and two boards are randomly generated.
The player can see where their ships are, indicated by @ sign, but cannot see where the computer's ships are.
Guesses are marked on the board with an X. Hits are indicated by *.
The player and computer then take turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponents's battleships first.

## Existing Features

- Random board generation
    - Ships are randomly placed on both the player and computer boards
    - The player cannot see where the computer's ships are

    - ![Random Board Generated](https://github.com/uchenna631/battleship-game/blob/main/assets/images/display-board.JPG?raw=true)

- Play against the computer
- Accepts user input
- Maintain scores

- image

- Input validation and error checking
    - You cannot enter the coordinates outside the size of the grid
    - You must enter digit numbers
    - You cannot enter the same guess twice

- Data maintained in class instance

## Future Features
- Allow player to select the board size and number of ships
- Allow player to position their ships themselves.
- Have ships larger than 1X1

## Data Model

I decided to use Board class as my model. The game creates two instances of the board class to hold the player's and the computer's board.

The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board and details such as the board type (player's board or computer) and the player's name

The class also has methods to help play the game, such as print method to print out the current board, an add_ships method to add ship to the board and an add_guess method to add guess and return the result.

## Testing

I have manually tested this project by doing the following:
- Passed the code through the PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bound inputs, same inpiut twice
- Tested in my local terminal and the Code Institute Heroku terminal

## Bugs
