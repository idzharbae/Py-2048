import numpy as np
import random

class bcolors:
	Red = '\u001b[41m'
	Green = '\u001b[42m'
	Yellow = '\u001b[43m'
	Blue = '\u001b[44m'
	Magenta = '\u001b[45m'
	Cyan = '\u001b[46m'
	White = '\u001b[47m'
	ENDC = '\033[0m'

def initialize_board(board_size):
	return [
		[0 for x in range(board_size)] for y in range(board_size)
	]

def rotate_counter_clockwise(mat, deg):
	arr = np.array(mat, int)
	arr = np.rot90(arr, deg / 90)
	return arr.tolist()

def move_up(arg, score):
	# avoid mutation of original data by copying
	board = [
		[x for x in y] for y in arg
	]
	n = len(board)
	for i in range(n):
		for j in range(n):
			for k in range(i+1, n):
				if board[k][j] == 0:
					continue
				if board[k][j] == board[i][j] or board[i][j] == 0:
					current_cell = board[i][j]

					board[i][j] += board[k][j]
					board[k][j] = 0

					if current_cell != 0: # merge happen
						score += current_cell
						break
					else:
						continue

				if i+1 == k:
					break
				board[i+1][j] = board[k][j]
				board[k][j] = 0
				break

	return board, score

def move_left(arg, score):
	# avoid mutation of original data by copying
	board = [
		[x for x in y] for y in arg
	]
	board = rotate_counter_clockwise(board, 270)
	board, score = move_up(board, score)
	board = rotate_counter_clockwise(board, 90)
	return board, score

def move_right(arg, score):
	# avoid mutation of original data by copying
	board = [
		[x for x in y] for y in arg
	]
	board = rotate_counter_clockwise(board, 90)
	board, score = move_up(board, score)
	board = rotate_counter_clockwise(board, 270)
	return board, score

def move_down(arg, score):
	# avoid mutation of original data by copying
	board = [
		[x for x in y] for y in arg
	]
	board = rotate_counter_clockwise(board, 180)
	board, score = move_up(board, score)
	board = rotate_counter_clockwise(board, 180)
	return board, score

def cell_coloring(cell_value):
	if cell_value < 2:
		return ''
	elif cell_value < 8:
		return bcolors.Blue
	elif cell_value < 64:
		return bcolors.Green
	elif cell_value < 512:
		return bcolors.Yellow
	elif cell_value < 2048:
		return bcolors.Magenta
	
	return bcolors.Red

def format_board(board):
	res = ''
	for row in board:
		s = ''
		for x in row:
			# s += '{:^5}'.format(x)
			color = cell_coloring(x) # remove this before running unit test
			s += color+'{:^5}'.format(x)+bcolors.ENDC
		res += s+'\n'
	return res

def print_board(board):
	print(format_board(board))

def check_win_condition(board, winning_value):
	for row in board:
		maxi = max(row)
		if maxi >= winning_value:
			return True
	return False

def check_lose_condition(board):
	if len(board) == 0:
		return False

	N = len(board[0])
	for i in range(N):
		for j in range(N):
			if board[i][j] == 0:
				return False
			if i-1 >= 0 and board[i][j] == board[i-1][j]:
				return False
			if i+1 < N and board[i][j] == board[i+1][j]:
				return False
			if j-1 >= 0 and board[i][j] == board[i][j-1]:
				return False
			if j+1 < N and board[i][j] == board[i][j+1]:
				return False
	return True

def spawn_number(arg):
	# avoid mutation of original data by copying
	board = [
		[x for x in y] for y in arg
	]
	N = len(board)
	empty_cells = []
	for i in range(N):
		for j in range(N):
			if board[i][j] == 0:
				empty_cells.append([i,j])

	r = random.randint(0, len(empty_cells)-1)
	i, j = empty_cells[r]
	board[i][j] = 2
	return board

def main():
	print('---------------------------- 2048 game ----------------------------')
	print('------------------------ exit with ctrl + c -----------------------')
	print()
	move_strategies = {'w': move_up, 'a' : move_left, 's': move_down, 'd': move_right}

	board_size = int(input('enter board size: '))
	winning_value = int(input('enter winning value: '))

	board = initialize_board(board_size)
	board = spawn_number(board)

	score = 0

	while True:
		board = spawn_number(board)
		if check_lose_condition(board):
			print('YOU LOSE!')
			exit()

		print('Score:', score)
		print()
		print_board(board)
		print()

		move = input('move: ')
		while move not in 'wasd' or len(move) < 0:
			print('invalid move!')
			move = input('move: ')[0]
		move = move[0]
		board, score = move_strategies[move](board, score)

		if check_win_condition(board, winning_value):
			print_board(board)
			print('YOU WIN!')
			exit()


if __name__=='__main__':
	main()