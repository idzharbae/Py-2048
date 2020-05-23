import game
import traceback

def test_initialize_board():
	board_size = 4
	board = game.initialize_board(4)

	assert(len(board) == 4)
	assert(len(board[0]) == 4)

def test_move():
	def check_result(board, score, expected_board, expected_score, f):
		print(f.__name__)
		result_board, result_score = f(board, score)
		print('\t\tboard:', board)
		print('\t\texpect:', expected_board)
		print('\t\tgot:', result_board)
		assert(result_board == expected_board)
		assert(result_score == expected_score)

	print('\ttesting: move without obstruction')
	score = 100
	board = [
		[2, 0, 0],
		[0, 0, 2],
		[0, 2, 0],
	]
	expected = [
		[2, 2, 2],
		[0, 0, 0],
		[0, 0, 0]
	]
	check_result(board, score, expected, 100, game.move_up)

	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 100, game.move_left)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 100, game.move_down)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 100, game.move_right)


	print('\ttesting: bumping with cells that have the same value')

	score = 90
	board = [
		[0, 2, 0],
		[0, 0, 0],
		[0, 2, 0]
	]
	expected = [
		[0, 4, 0],
		[0, 0, 0],
		[0, 0, 0]
	]
	check_result(board, score, expected, 92, game.move_up)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 92, game.move_left)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 92, game.move_down)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 92, game.move_right)

	print('\ttesting: multiple cells in a column have the same value')
	score = 99
	board = [
		[0, 2, 0],
		[0, 2, 0],
		[0, 2, 0]
	]
	expected = [
		[0, 4, 0],
		[0, 2, 0],
		[0, 0, 0]
	]
	check_result(board, score, expected, 101, game.move_up)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 101, game.move_left)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 101, game.move_down)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 101, game.move_right)

	score = 10
	board = [
		[0, 2, 0, 0],
		[0, 4, 0, 4],
		[0, 2, 0, 4],
		[0, 2, 0, 4],
	]
	expected = [
		[0, 2, 0, 8],
		[0, 4, 0, 4],
		[0, 4, 0, 0],
		[0, 0, 0, 0],
	]
	check_result(board, score, expected, 16, game.move_up)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 16, game.move_left)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 16, game.move_down)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 16, game.move_right)

	print('\ttesting: cells with different value')
	score = 1000
	board = [
		[0, 0, 0],
		[0, 8, 0],
		[0, 2, 0]
	]
	expected = [
		[0, 8, 0],
		[0, 2, 0],
		[0, 0, 0]
	]
	check_result(board, score, expected, 1000, game.move_up)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 1000, game.move_left)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 1000, game.move_down)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 1000, game.move_right)

	score = 123
	board = [
		[0, 16, 0],
		[0, 0, 0],
		[0, 4, 0]
	]
	expected = [
		[0, 16, 0],
		[0, 4, 0],
		[0, 0, 0]
	]
	check_result(board, score, expected, 123, game.move_up)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 123, game.move_left)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 123, game.move_down)
	board = game.rotate_counter_clockwise(board, 90)
	expected = game.rotate_counter_clockwise(expected, 90)
	check_result(board, score, expected, 123, game.move_right)

def test_format_board():
	board = [
		[1, 1337, 2],
		[69, 13, 42],
		[4, 2, 0]
	]
	s = game.format_board(board)
	expected = '  1  1337   2  \n 69   13   42  \n  4    2    0  \n'
	assert(expected == s)

def test_winning_condition():
	board = [
		[1, 1337, 2],
		[69, 13, 42],
		[4, 2, 0]
	]
	res = game.check_win_condition(board, 1337)
	assert(res == True)
	res = game.check_win_condition(board, 1336)
	assert(res == True)
	res = game.check_win_condition(board, 1338)
	assert(res == False)

def test_losing_condition():
	board = [
		[1, 1337, 2],
		[69, 13, 42],
		[4, 2, 1]
	]
	res = game.check_lose_condition(board)
	assert(res == True)
	board = [
		[1, 1337, 2],
		[69, 13, 42],
		[4, 2, 0]
	]
	res = game.check_lose_condition(board)
	assert(res == False)

	board = [
		[1, 1337, 2],
		[69, 1337, 42],
		[4, 2, 1]
	]
	res = game.check_lose_condition(board)
	assert(res == False)
	board = [
		[1, 1337, 2],
		[69, 13, 42],
		[4, 1337, 1]
	]
	res = game.check_lose_condition(board)
	assert(res == True)

def test_spawn_number():
	count_board_sum = lambda board : sum([sum(x) for x in board])

	board = [
		[0, 16, 0],
		[0, 0, 0],
		[0, 4, 0]
	]
	res = game.spawn_number(board)
	assert(count_board_sum(res) == count_board_sum(board) + 2)
	assert(res[0][1] == 16)
	assert(res[2][1] == 4)

	board = [
		[0, 16, 0],
		[3, 5, 96],
		[0, 4, 0]
	]
	res = game.spawn_number(board)
	assert(count_board_sum(res) == count_board_sum(board) + 2)
	assert(res[0][1] == 16)
	assert(res[1] == [3, 5, 96])
	assert(res[2][1] == 4)

	board = [
		[7, 16, 1],
		[8, 10, 110],
		[9, 4, 0]
	]
	res = game.spawn_number(board)
	assert(count_board_sum(res) == count_board_sum(board) + 2)
	assert(res == [
		[7, 16, 1],
		[8, 10, 110],
		[9, 4, 2]
	])

def main():
	tests = [
		test_initialize_board,
		test_move,
		test_format_board,
		test_winning_condition,
		test_losing_condition,
		test_spawn_number
	]
	for test in tests:
		test = logger_wrap(test)
		test = handle_assert_exception_wrap(test)
		test()

def handle_assert_exception_wrap(f):
	def h():
		try:
			f()
		except AssertionError as err:
			print('Test fail: %s' % f.__name__)
			traceback.print_tb(err.__traceback__)
	return h

def logger_wrap(f):
	def h():
		print('Running test: %s' % f.__name__)
		f()
		print('Test passed.')
	return h


if __name__=='__main__':
	main()