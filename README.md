# MinesweeperSolver

This project is an automated Minesweeper solver developed using Selenium WebDriver and Python. The solver interacts with a web-based Minesweeper game by identifying cell types, marking mines, and clicking on safe cells based on the rules of the game. It leverages an efficient algorithm to track adjacent cell counts and determine which cells are safe to click and which are potential mines.

Features:

Web Automation: Uses Selenium WebDriver to interact with the Minesweeper game, automatically clicking cells and marking mines.
Flagging Mines: Identifies and flags potential mines based on neighboring cell numbers.
Pattern Recognition: Analyzes surrounding cells and applies logic to safely click unopened cells or mark mines.
Flexible Grid Size: Supports standard 9x9 grids but can be easily adapted for larger grids.
Automation of Moves: Automatically clicks through the grid based on discovered clues to minimize manual intervention.
Visual Representation: The solver prints a visual representation of the current state of the game.

Technologies Used:

Selenium WebDriver: For web automation and interaction with the Minesweeper game.
BeautifulSoup: For parsing and scraping additional elements (if needed).
ActionChains: For simulating mouse clicks and context clicks (right-click) to flag potential mines.

How It Works:

Grid Analysis: The program identifies the cells that are unopened, flagged, or contain numbers (indicating adjacent mines).
Mine Flagging: Based on surrounding numbers, it flags cells that are suspected to be mines.
Safe Clicking: Safely clicks cells when it is certain they are not mines.
Recursive Strategy: Continues the process until the puzzle is solved or no more safe moves can be made.

**Installation:**

Clone the repository:

    git clone https://github.com/ilham3169/MinesweeperSolver.git

Install dependencies:

    pip install -r requirements.txt

Run the solver:

    python main.py
