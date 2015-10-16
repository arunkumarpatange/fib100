

import heapq

class Merge:
	data = []

	@classmethod
	def insert(cls, list):
		for n in list:
			heapq.heappush(cls.data, n)

	@classmethod
	def sorted_array(cls):
		while cls.data:
		 yield heapq.heappop(cls.data) 

Merge.insert([1, 4, 6])
Merge.insert([1, 1, 3])
Merge.insert([1, 2, 3])

print [ n for n in  Merge.sorted_array() ]


def version (v1, v2):
	split = "."
	try:
		_v1, _v2 = int("".join(v1.split(split))), int("".join(v2.split(split)))
		if  _v1 > _v2: return 1
		if  _v1 == _v2: return 0
		if  _v1 < _v2: return -1
	except ValueError:
		raise Exception("not a valid integer (%s) (%s)" % (v1, v2))

print version("1.0.1.1", "1.0.1.1")
print version("1.0.1.2", "1.0.1.1")
print version("1.0.1.2", "10.0.1.1")
print version("asd", "1.1")

