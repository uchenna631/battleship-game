#   THE ULTIMATE BATTLESHIP

The Ultimate Battleship is a python terminal game which runs on the Code Institute's mock terminal Heroku

Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one square on the board

[Here is the live version of my project](https://the-ultimate-battleship.herokuapp.com/)

![Front-end view](https://github.com/uchenna631/battleship-game/blob/main/assets/images/front-%20end-view.JPG?raw=true)

## How to play
Battleship is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet. You can read more about it on [wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version, the player chooses the board size, the number of ships and enter's their name. Two boards are then randomly generated.
The player can see where their ships are, indicated by "@" sign, but cannot see where the computer's ships are.
Guesses are marked on the board with an "X". Hits are indicated by "*".
The player and computer then take turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponents's battleships first.

## Existing Features

- Random board generation
    - Ships are randomly placed on both the player and computer boards
    - The player cannot see where the computer's ships are

    ![Random Board Generated](https://github.com/uchenna631/battleship-game/blob/main/assets/images/display-board.JPG?raw=true)

- Play against the computer
- User can choose the board size and the number of ships

    ![Request user input](https://github.com/uchenna631/battleship-game/blob/main/assets/images/requests-user-input.JPG?raw=true)
    
- Accepts user input
- Maintain scores

    ![Play against the computer](https://github.com/uchenna631/battleship-game/blob/main/assets/images/play-against-computer.JPG?raw=true)

- Input validation and error checking
    - You can only choose integers within limits as the size of board and the number of ships.
    - Player can only enter alphabets as their name
    
    ![Size, num_ship, player_name validation](https://github.com/uchenna631/battleship-game/blob/main/assets/images/board-size_num-ships_validation.JPG?raw=true)

    - You cannot enter the coordinates outside the size of the grid
    - You must guess digit numbers as board coordinates
    - You cannot enter the same guess twice

    ![Input validation](https://github.com/uchenna631/battleship-game/blob/main/assets/images/input-validation.JPG?raw=true)

- Data maintained in class instance

## Future Features
- Allow player to position their ships themselves.
- Have ships larger than 1X1

## Data Model

I decided to use Board class as my model. The game creates two instances of the board class to hold the player's and the computer's board.

The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board and details such as the board type (player's board or computer) and the player's name

The class also has methods to help play the game, such as print method to print out the current board, an add_ships method to add ship to the board and an add_guess method to add guess and return the result.

## Testing

I have manually tested this project by doing the following:
- Passed the code through the PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bound inputs, same input twice
- Tested in my local terminal and the Code Institute Heroku terminal

## Bugs

### Solved Bugs

- When I finished the project, the player's guess was being appended on the player's board whereas the computer's guess was also appended on the computer's board. This was resolved by modifying the guess method.
- The player's input name was accepting empty string's and number as player's name. This was resolved by adding some input validation.

### Remaining Bugs
- No bugs remaining

## Validator Testing

### PEP8 
- The following errors were found and resolved
    - Blank lines: this was resolved by adding two blank lines before and after each class or a function
    - Trailing whitespace: this was resolved by removing whitespaces at the end of lines and on blank lines.
    - Continuation line under-indented for visual indent
- No pending error

![PEP8 report](https://github.com/uchenna631/battleship-game/blob/main/assets/images/PEP8%20result.JPG?raw=true)

## Deployement

This project was deployed manually from Gitpod command line interface using the Code Institute's mock terminal for Heroku 

Steps for deployment
- Creating a Heroku Account/App
    - Create/login into a Heroku account.
    - Click "New" menu and select "Create new app"
    - Fill out the form; choosing a unique app name and region. Click on "Create app"
- Configuration
    - Click on the settings menu
    - Add PORT to Config Vars and set its value to 8000
    - Set the buildpacks to Python and NodeJS
- Deploying from Gitpod CLI
    1. Login to Heroku and enter your details. command: "heroku login-i"
    2. Get your app name from heroku
    command: "heroku apps"
    3. Set the heroku remote (Replace app_name with your unique app name). Command: "heroku git:remote -a <app_name>"
    4. Add, commit and push to Github.
    command: "git add ." and "git commit -m'Deploy to Heroku via CLI'"
    5. Push to both Github and Heroku
    command: "git push" 
    command: "git push heroku main"

## Credit

- Code Institute's tutorial on battleship game and README.md file
- Code Institute for the deployment termial
- Mentor - Spencer Barriball for his insight, support and guidance