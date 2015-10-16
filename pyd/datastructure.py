class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left or None
		self.right = right or None

class Stack(object):

	MAX = 20

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)
		return self

	def pop(self):
		if len(self.items) != 0:
			item = self.items[-1]
			self.items = self.items[:-1]
			return item


class Hash(object):

	MAX = 100
	@classmethod
	def hash(cls, input):
		return sum(map(ord, str(input)))  % cls.MAX

	def __init__(self):
		self.hashed = [[] for i in range(self.MAX)]

	def _find(self, key):
		hash = self.hash(key)
		return next(((_key, v) for (_key, v) in self.hashed[hash] if _key == key), None)

	def put(self, item, v=None):
		hash = self.hash(item)
		self.hashed[hash].append((item, v or item))
		return self

	def get(self, item):
		v = self._find(item)
		if v is None:
			assert False,  'no key error'
		return v



class PQ(object):

	@classmethod
	def heapify(cls, array):
		return cls(array)

	def __init__(self, array):
		pass
#print "adadf".count('ad')
#print "adadf".count.__doc__

class Ufind:
	'''
		 0 1  2 
		-1 0 -1
	'''


	def __init__(self, length):
		self.length = length
		self.store = [-1] * length

	def find(self, index):
		if self.store[index] == -1:
			return index
		return self.find(self.store[index])

	def union(self, a, b):
		x = self.find(a)		
		y = self.find(b)		
		if x != y:
			self.store[x] = y
		return self

if __name__ == "__main__":

	print (
		Ufind(4).union(0, 1)
			.union(2, 1).union(2, 1).union(1, 2).union(2, 0)
			.union(3, 0).union(3, 1).union(3, 2).union(3, 2)
			.store
	)

	h = Hash()
	h.put(1)
	h.put('r', 'r')
	h.put(99)
	h.put(1001)
	print h.get(1)
	print h.get(99)
	print h.get(1001)
	print h.get('r')
