# Battleship Game

The battlefield game is played on a 10x10 square playing surface. On this plane, ships with a specified number of squares are positioned. Two players try to guess the location of opposing ships, shoot at them, and sink them. Battleships is a Python-based game in which players strategically position their battleships on the board and attack the fleet of their opponent in turn. A web-based multiplayer mode and a single-player mode against an AI opponent are among the game's many play modes.


### Game Rules
- Each participant arranges their ships on their own grid prior to the start of the game without disclosing the arrangement to their opponent. The ships differ in dimensions; typically, each participant possesses five ships. Examples of typical ship types include:
Aircraft Carrier (5 spaces)
Battleship (4 spaces)
Cruiser (3 spaces)
Submarine (3 spaces)
Destroyer (2 spaces)
The objective of this game is for players to identify an attack location on the opponent's grid by reciting specific grid coordinates in turn. "Hit" or "Miss" are the opponent's responses, respectively, if the coordinate belonged to a ship or an unoccupied space. Alternating blasts are continued by all participants until one's entire fleet is submerged.
Achieving success in Battleship requires both strategic deduction and good fortune. A player's strategy for targeting the opponent's ships is to methodically analyse past hits and misses. 
"Winning" is determined when one participant destroys the opponent's entire fleet. 


## Features
- Board Initialization: Use the initialise_board function to create an empty game board with a default size of 10x10.
- Battleship Configuration: Invoke the create_battleships function to retrieve a dictionary containing the dimensions of battleships from a configuration file (battleships.txt by default).
- Battleship Placement: Utilise the place_battleships function to allocate battleships to the board. It provides support for simple, random, or custom placement algorithms.
- Game Loop: Play a simple single-player game loop in which the player takes turns assaulting and attempting to sink the AI opponent's fleet.
-Web Interface: Use Flask to create a web-based interface for both the Battleships Placement page and the Gameplay page.
- Coordinate Input: Accept user input for attack coordinates in the web interface using the cli_coordinates_input function.
- AI Opponent: Challenge an AI opponent in a strategic battle with a customizable game loop.
- Multiplayer Interface: Create a multiplayer interface with separate webpages for battleship placement and gameplay.


## File Layout
```
battleships_game/
│
├── components/
│   ├── __init__.py
│   ├── initialise_board.py
│   ├── create_battleships.py
│   └── place_battleships.py
│
├── game_engine/
│   ├── __init__.py
│   ├── attack.py
│   ├── cli_coordinates_input.py
│   ├── simple_game_loop.py
│   ├── generate_attack.py
│   └── ai_opponent_game_loop.py
│
├── mp_game_engine/
│   ├── __init__.py
│   └── multiplayer_functions.py
│
├── templates/
│   ├── placement.html
│   └── main.html
│
├── static/
│   └── style.css
│
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

## Module and Code Explanations

- components.py: Basic components to set up the battleships game.

  - initialise_board(size)
    - This function creates a board with size x size items and a size parameter that has been predefined -in the txt format, and returns it.

  - create_battleships(filename)
    - this function returns the battleships.txt file which includes the type and size of the ships.

  - place_battleships(board, ships, algorithm)
    - This function places specified ships onto a board in whatever 
    chosen algorithm: simple, random or custom.


- game_engine.py: By utilising the setup components found in components.py, this module implements single-player game functionality for the game. 

  - attack(coordinate, board, battleships):
    -  For the corresponding assault, implement the function that verifies whether or not a battleship is present at that coordinate on the board.

  - cli_coordinates_output()
    - Solicits a letter-number input from the user via the command line; returns a tuple containing the specified values in tuple format.

  - simple_game_loop()
    - to test the funcionality of code in components


- mp_game_engine.py: this is a module which allows us to play in multiplayer mode

  - generate_attack()
    - Generates a random tuple attack.

  - ai_opponent_game_loop()
    - This AI game loop enables multiplayer play versus an AI opponent.

- main.py: This module manages the web deployment of my Flask server, which enables interactive battleships on a dynamic website. This transitions the game from a cli to a web-based format.

  - placement_interface()
    - After confirming the user-selected ship configuration, this method permits its placement and returns the user to the root with the updated data.

  - root()
    - Presents the homepage of the specified URL, which includes the current player board and the primary gameplay template.

  - game_attack()
    - process the attack and continues the game loop. İt is esssential to store the data since it is arranging it and updating the board each time. That's why the session extension of flask has been used here. 

##Self-Assessment
This project showcases a resilient implementation of the game Battleships, incorporating functionalities such as the positioning of battleships, strategic gameplay against an artificial intelligence opponent, and a user-friendly online interface. The programme exhibits a well-organized structure, providing ample flexibility in terms of setup and gaming algorithms. The inclusion of a multiplayer option enriches the game experience, elevating it to a more captivating and pleasurable endeavour. The goal of creating a dynamic and captivating gaming experience has culminated in the Battleships project. The project's core features demonstrate a dedication to user interaction, modularity, and high-quality code.


### Author
Zeynep Guler

### License
[MIT](https://choosealicense.com/licenses/mit/)
MIT License

Copyright (c) [2023] [Zeynep Guler]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.