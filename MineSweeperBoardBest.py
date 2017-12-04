"""
Rohin Shivdasani HW 10/15/17

Minesweeper Board

Sources: Looked at Ms. Healey's code and tyred to model parts of mine after hers. Used her example to fix my not working vresion.
		Lam Tran Bach - He helped me with coming up for the method of searching surrounding spaces to check if there is a bomb (before we went over it in class today).
		He also just helped me try to figure out some errors, like the list index out of range error (but to no avail).

Notes: Functionally, I think it works perfect, but since I used -1 to represent a bomb, the board is hard to look at visually beciase -1 is two characters, whereas all the other numbers in the board are one character, so it shifts things out of place when there is a bomb. I can try and fix this in the near future by using a star or something as my bomb.
"""


import random
import sys

n = int(sys.argv[1]) #n is number of rows
m = int(sys.argv[2]) #m is number of columns
b = int(sys.argv[3]) #bombs = b

# create an empty board
board = []
for i in range(0, n+2):
	row = [0]*(m+2)
	board.append(row)

# put bombs on board
for i in range(b):
	x = random.randint(1,n)
	y = random.randint(1,m)
	while board[x][y] == -1:
		x = random.randint(1,n)
		y = random.randint(1,m)
	board[x][y] = -1

#-1 means there is a bomb there

for i in range (1,n+1): 
	for j in range (1,m+1): 
		if (board[i][j] == 0):
			if (board[i-1][j-1] == -1):
				board[i][j] += 1
			if ( board[i-1][j] == -1):
				board[i][j] += 1
			if ( board[i-1][j+1] == -1):
				board[i][j] += 1
			if (board[i][j-1] == -1):
				board[i][j] += 1
			if (board[i][j+1] == -1):
				board[i][j] += 1
			if ( board[i+1][j-1] == -1):
				board[i][j] += 1
			if ( board[i+1][j] == -1):
				board[i][j] += 1
			if ( board[i+1][j+1] == -1):
				board[i][j] += 1



def matrixprintswag(board):
	for row in range(1, len(board)-1):
		for col in range(1, len(board[0])-1):
			print(board[row][col], end=' ')
		print('')



matrixprintswag(board)