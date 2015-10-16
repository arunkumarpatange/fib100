
import unittest
from pyd.maze import *


class MirrorTest(unittest.TestCase):

	def test_mirror_types(self):
		self.assertEqual(set(Mirror.get_mirrors().keys()), {'/', '\\'})
		self.assertEqual(Mirror.get_by_name('/').name, '/')
		self.assertEqual(Mirror.get_by_name('\\').name, '\\')

	def test_direction_forward_mirror(self):
		mirror = Mirror.get_by_name('/')
		mirror = mirror((1, 5))
		expected = (
			(Direction.North, Direction.East),
			(Direction.South, Direction.West),
		) 
		for incident, redirect in expected:
			self.assertEqual(mirror.get_direction(incident), redirect)
			self.assertEqual(mirror.get_direction(redirect), incident)


class LaserTest(unittest.TestCase):

	def test_no_loop(self):

		laser = Laser((1, 1), Direction.North)
		laser.set_pos((0, 1))

		self.assertEqual(laser.get_trail(), [(1, 1), (0, 1)])
		self.assertEqual(laser.directions, [Direction.North] * 2)
		# no mirror
		laser.set_direction(Direction.South)
		self.assertFalse(laser._revisiting((1, 1)))


	def test_loop(self):
		'''
			/  		\

			\  		/

		'''
		_ = [(2, 1), (1, 1), (1, 2), (3, 2), (3, 1),]

		laser = Laser(_[0], Direction.North)
		laser.set_pos(_[1])
		laser.set_direction(Direction.East)
		laser.set_pos(_[2])
		laser.set_direction(Direction.South)
		laser.set_pos(_[3])
		laser.set_direction(Direction.West)
		laser.set_pos(_[4])

		self.assertEqual(laser.get_trail(), _)
		self.assertEqual(laser.directions, list('NNESW'))

		laser.set_pos((1, 1))
		laser.set_direction(Direction.East)
		self.assertTrue(laser._revisiting((1, 1)))

	def test_loop2(self):
		'''
					/ - - - \
					|		|
			/ - ->  /		|
			|				|
			\ - - - - - - - /

		'''
		_ = [(3, 2), (3, 3), (1, 3), (1, 4), (4, 4), (4, 1), (3, 1), (3, 3)]
		directions = list('EENESWNE')
		laser = None
		for pos, direction in zip(_, directions):
			if laser is None:
				laser = Laser(pos, direction)
			else:
				laser.set_direction(direction)
				laser.set_pos(pos)

		self.assertEqual(laser.get_trail(), _)
		self.assertEqual(laser.directions, list('EENESWNE'))

		# change direction not called, so no loop
		self.assertFalse(laser._revisiting((3, 3)))
		# set direction called
		laser.set_direction(Direction.North)
		self.assertTrue(laser._revisiting((3, 3)))



class BoardTest(unittest.TestCase):

	def test_board_simple(self):
		for pos, direction in zip([(3, 3), (4, 2), (3, 1), (2, 2)], 'NESW'):
			board = Board(6, 6)
			board.add_laser((3, 2), direction)
			self.assertEqual(next(board.get_next_pos()), pos)


	def test_laser_position(self):
		'''
			no mirrors
		'''
		board = Board(6, 6)
		board.add_laser((3, 2), Direction.East)

		trails = board.get_laser_position()
		self.assertEqual(list(trails), [(4, 2), (5, 2)])

	def test_laser_with_mirror(self):

		board = Board(6, 6)
		board.add_laser((2, 3), Direction.East)
		board.add_mirror(Forward((4, 3)))

		trails = board.get_laser_position()
		self.assertEqual(next(trails), (3, 3))
		self.assertEqual(board.laser.direction, Direction.East)
		self.assertEqual(next(trails), (4, 3))
		self.assertEqual(board.laser.direction, Direction.East)
		self.assertEqual(next(trails), (4, 4))
		self.assertEqual(board.laser.direction, Direction.North)

	def test_mirror_loop(self):
		'''
					/ - - - \
					|		|
			/ - ->  /		|
			|				|
			\ - - - - - - - /

		'''
		F, B = Forward, Backward
		mirrors = [F((3, 2)), F((3, 4)), B((4, 4)), F((4, 1)), B((1, 1)), F((1, 2))]
		board = Board(6, 6)
		board.add_laser((2, 2), Direction.East)
		for mirror in mirrors:
			board.add_mirror(mirror)

		trails = list(board.get_laser_position())
		# has loop
		self.assertEqual(trails[-1], (-1, -1))
		self.assertEqual(len(trails) - 1, 13)

	def test_mirror_loop2(self):
		'''
					/ - - - \
					|		|
			/ - ->  / - - - /
			|		|
			\ - - - /

		'''
		F, B = Forward, Backward
		mirrors = [F((3, 2)), F((3, 4)), B((4, 4)), F((4, 2)), F((3, 1)), B((1, 1)), F((1, 2))]
		board = Board(6, 6)
		board.add_laser((2, 2), Direction.East)
		for mirror in mirrors:
			board.add_mirror(mirror)

		trails = list(board.get_laser_position())
		# has loop
		self.assertEqual(trails[-1], (-1, -1))
		self.assertEqual(len(trails) - 1, 13)

	def test_boundary_loop(self):
		F, B = Forward, Backward
		mirrors = [B((0, 0)), F((0, 3)), B((3, 3)), F((3, 0))]
		board = Board(4, 4)
		board.add_laser((0, 1), Direction.North)
		for mirror in mirrors:
			board.add_mirror(mirror)

		trails = list(board.get_laser_position())
		# has loop
		self.assertEqual(trails[-1], (-1, -1))
		self.assertEqual(len(trails) - 1, 14)

	def test_boundary(self):
		'''
			- - -> /
		'''
		F, B = Forward, Backward
		mirrors = [B((0, 2))]
		board = Board(4, 4)
		board.add_laser((0, 1), Direction.North)
		for mirror in mirrors:
			board.add_mirror(mirror)

		trails = list(board.get_laser_position())
		self.assertEqual(trails, [(0, 2),])


if '__main__' == __name__:
	unittest.main()
