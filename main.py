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

""" You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!

"""
