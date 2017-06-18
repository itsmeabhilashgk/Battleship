from random import randint
board = []
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for x in board:
        print (" ".join(x))
print_board(board)

def randgenerator(board):
	return (randint(0,len(board) - 1))

rand_row = randgenerator(board)
rand_col = randgenerator(board)
win = 0
for turn in range(5):
	guess_row = int(input("Guess Row:"))
	guess_col = int(input("Guess Column:"))
	if rand_row == guess_row and rand_col == guess_col:
		print("CONGRATS! You just destroyed my Battleship") 
		board[rand_row][rand_col] = "X"
		print_board(board)
		break
		win = 1
	elif guess_row not in range(5) or guess_col not in range(5):
		print("You are far to away from my battleship!")
	elif board[guess_row][guess_col] == "X":
		print("You have already guessed that!")
		print_board(board)
	else:
		board[guess_row][guess_col] = "X"
		print("That's not my Battleship")
		print_board(board)

if win = 1:
	print("YOU WIN!")
else:
	print("You failed to guess where my Battleship is! You freakin loose Sucker!")
	print("This was where my BattleShip was:")
	for x in range(5):
		for i in range(5):
			board[x][i] = "O"	
	board[rand_row][rand_col] = "X"
	print_board(board)


