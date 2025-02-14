# Tic Tac Toe - Command Line Game

This is a simple command-line Tic Tac Toe game built using Python. It allows two players to take turns and compete in the classic game of Tic Tac Toe.

## Features
- Two-player mode.
- Clear and simple user prompts.
- Random selection of which player goes first.
- Board display updates after every move.
- Prompt is repeated if incorrect input is given or marker is already taken.
- Win, draw, and replay functionality.

## Requirements
- Python 3.x

## How to Run
1. Clone this repository or download the source files.
2. Navigate to the project directory.
3. Run the following command:

```bash
python main.py
```

## Game Rules
- The game is played on a 3x3 grid.
- Players take turns choosing positions on the grid (1-9).
- A player wins by placing three of their markers (X or O) in a row, column, or diagonal.
- If all spaces are filled and no player has won, the game is a draw and replay is initiated.

## Board Placement Layout
```
 7 | 8 | 9
---|---|---
 4 | 5 | 6 
---|---|---
 1 | 2 | 3
```  

## Project Structure
```
tic_tac_toe/
│
├── tic_tac_toe/
│   ├── __init__.py
│   ├── board.py
│   ├── player.py
│   ├── game.py
│   └── utils.py
│
├── main.py
└── README.md
```

## Description of Files
- **board.py:** Functions for displaying and updating the board.
- **player.py:** Handles player input and turn management.
- **game.py:** Main game loop and logic.
- **utils.py:** Utility functions (e.g., replay prompt, clearing screen).
- **main.py:** Entry point to start the game.
- **original_tic_tac_toe.py** Original single page script that project was based on.

## Example Output
```
Player 1: Choose X or O: X
Player 1 goes first.
Ready to play? (Yes/No): Yes
  X |   | O
 ---|---|---
  O | X |  
 ---|---|---
  X | O | X
Congratulations! Player 1 wins!
Play again? (Yes/No): No
Thanks for playing!
```

## Future Improvements
- Improve the board refresh mechanism.
- Add single-player mode with AI.
- Implement error handling for invalid inputs.
- Add a graphical user interface (GUI).
- If player choses marker that is already taken return 'Marker is already taken, please pick another one.' and return position choice prompt.

## Improvements Made
- Added clear screen function which brings refresh mechanism to 0.5 seconds (02/14)

## Author Note
I took the original single page script for the Milestone Project 1 with Udemy's Complete Python3 Bootcamp and applied proper application structure in order to demonstrate:
- Separation of Concerns: Each module has a clear responsibility.
- Reusability: Functions and components can be reused and tested independently.
- Scalability: Easier to extend or swap parts of the application, like adding AI or networked multiplayer.
- Readability: Easier to understand and maintain the code.

## License
This project is licensed under the MIT License.

## Author
Gabriel L. Rodriguez Perez

