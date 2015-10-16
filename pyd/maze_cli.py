
import sys

from maze import Board


def maze_player():
	in_file, out_file = sys.argv[1:]

	board = Board.get_layout(in_file)
	with open(out_file, 'w') as f:
		positions = list(board.get_laser_position())
		if positions[-1] == (-1, -1):
			f.write(-1)
		else:
			f.write(str(len(positions)) + '\n')
			f.write(str(positions[-1]))


maze_player()
