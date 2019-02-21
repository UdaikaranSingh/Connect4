# Connect4

This code is made to implement a useable Connect4 board (to be played in terminal), and apply a self-implemented Minmax algorithm (with a/b pruning) on the associated game tree.

The inspiration for this idea came from this video: https://www.youtube.com/watch?v=yDWPi1pZ0Po

The video claims that the player with the first move is guaranteed to win the game. Therefore, this would imply that when applying the Minimax algorithm, there will be a path from the root node to a terminal node such that the player with the first turn wins no matter the moves made by the opponent.

The reason Connect4 is choosen is because the max-depth of the tree is 42 (board size is 6x7) and the fan-out for each node is <= 7. This makes Connect4 a significantly easier problem than other games such as Chess, which has a fan-out of over 20 in many cases, and an infinite depth.


Description of Code:
  Connect4.py = implementing the Connect4 board
  MiniMax.py = implementing the game tree & Minimax algorithm
  Connect 4 With MiniMax Implementation.ipynb = notebook to run/test code
  
