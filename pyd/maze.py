
class Direction(object):
	North = 'N'
	South = 'S'
	East = 'E'
	West = 'W'


class Mirror(object):

	@classmethod
	def get_name(cls):
		return getattr(cls, 'name', None)

	@classmethod
	def get_doi(cls):
		return getattr(cls, 'doi', None)

	@classmethod
	def get_mirrors(cls):
		return {
			mirror.get_name(): mirror
			for mirror in cls.__subclasses__()
		}

	@classmethod
	def get_by_name(cls, name):
		for _name, mirror in cls.get_mirrors().iteritems():
			if name == _name:
				return mirror

	def __init__(self, position):
		self.position = position

	def get_direction(self, doi):
		'''
			doi: direction of incidence
		'''
		for doi_set in self.get_doi():
			if doi in doi_set:
				return (doi_set - set(doi)).pop()


class Forward(Mirror):
	name = '/'
	# direction of incidence
	doi = (
		{Direction.North, Direction.East},
		{Direction.South, Direction.West},
	)

class Backward(Mirror):
	name = '\\'
	doi = (
		{Direction.North, Direction.West},
		{Direction.South, Direction.East},
	)

class Laser(object):

	def __init__(self, start, direction):
		self.directions = [direction,]
		self.trail = [start,]
		self.pos = self.trail[-1]
		self.direction = self.directions[-1]

	def set_pos(self, pos):
		self.trail.append(pos)
		self.directions.append(self.direction)
		self.pos = self.trail[-1]

	def set_direction(self, direction):
		# self.directions.append(direction)
		assert direction is not None
		self.direction = direction

	def _revisiting(self, _pos):
		# check loops
		for i, pos in enumerate(self.trail[:-1], start=1):
			if self.trail[-i - 1] == _pos:
				if self.directions[-i] == self.direction:
					return True

	def get_trail(self): return self.trail


class Board(object):

	@classmethod
	def get_layout(cls, file):
		with open(file) as f:
			board = None
			for line in f.read().splitlines():
				line = line.split()
				board = board or cls(int(line[0]), int(line[1]))
				if board and line[-1] == 'S':
					xy = tuple(int(coord) for coord in line[:-1])
					board.add_laser(xy, line[-1])

				if board and line[-1] in Mirror.get_mirrors():
					xy = tuple(int(coord) for coord in line[:-1])
					board.add_mirror(Mirror.get_by_name(line[-1])(xy))
			return board

	def __init__(self, row, col):
		self.layout = (int(row), int(col))
		self.laser = None
		self.mirrors = {}

	def add_laser(self, position, direction):
		if self.laser is None:
			self.laser = Laser(position, direction.upper())
		return self

	def add_mirror(self, mirror):
		assert mirror.position != self.laser.pos, 'mirror not allowed at laser position'
		self.mirrors.update({mirror.position: mirror})

	def get_next_pos(self):
		wallx, wally = self.layout
		while True:
			x, y = self.laser.pos
			mirror = self.mirrors.get((x, y), None)
			if mirror is not None:
				self.laser.set_direction(mirror.get_direction(self.laser.direction))
				if self.laser._revisiting((x, y)):
					yield (-1, -1) # in loop
					break

			if self.laser.direction == Direction.West:
				if x - 1 < 0:
					break
				yield x - 1, y
			elif self.laser.direction == Direction.East:
				if x + 1 > wallx - 1:
					break
				yield x + 1, y
			elif self.laser.direction == Direction.North:
				if y + 1 > wally - 1:
					break
				yield x, y + 1
			elif self.laser.direction == Direction.South:
				if y - 1 < 0:
					break
				yield x, y - 1

	def get_laser_position(self):
		for pos in self.get_next_pos():
			self.laser.set_pos(pos)
			yield pos
