######################################
# Connect4 Game Board
# By: Udaikaran Singh
# Date Started: 2/16/19
######################################
import numpy as np

class Connect4:
	dimension = 7
	#players are either "X" or "O"

	def __init__(self, x = 7):
		#board represented by array length 7, each containing an array of length 7
		#first input = row
		#2nd input = column
		self.columns = ["*"] * self.dimension
		for i in range(self.dimension):
			self.columns[i] = (["*"] * ((self.dimension-1)))

	def showBoard(self):
		for i in range(self.dimension)[::-1]:
			print(self.columns[i])

	def clearBoard(self):
		self.columns = ["*"] * self.dimension
		for i in range(self.dimension):
			self.columns[i] = (["*"] * ((self.dimension-1)))

	def placePiece(self, i, player):
		assert (type(i) == int)
		assert (type(player) == str)

		if (player == "Player 1"):
			turn = "X"
		elif (player == "Player 2"):
			turn = "O"

		for col in range(self.dimension):
			if (self.columns[col][i] == "*"):
				self.columns[col][i] = turn
				return
		print ("Turn not Valid")


	def checkWin(self):
		...

	def _checkHorizontalWin(self):
		...

	def _checkVerticalWin(self):
		...

	def _checkDiagonalWin(self):
		...
