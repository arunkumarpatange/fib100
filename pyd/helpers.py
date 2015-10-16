from pyd.datastructure import Node

class Bst(object):

	class Node:
		def __init__(self, val):
			self.val = val
			self.left = None
			self.right = None

	def __init__(self):
		self._root = None

	def add(self, val):
		def _add(val, _root):
			if _root is None:
				_root = self.Node(val)
			elif _root.val < val:
				_right = _add(val, _root.right)
				_root.right = _right
			else:
				_left = _add(val, _root.left)
				_root.left = _left
			return _root

		self._root = _add(val, self._root)
		return self._root

def get_tree(default=None, cls=None):
	'''
			 8
		  /     \
		4        10
	  /   \     /  \
	1      5   9    11
	'''
	default = default or [8, 4, 10, 1, 5, 9, 11]
	_bst =  (cls or Bst)()
	for n in default:
		_bst.add(n)

	# root
	if cls:
		return _bst
	return _bst._root

import random
def randomize(l):
	for i in xrange(len(l)):
		j = random.randint(0, len(l) - 1)
		l[i], l[j] = l[j], l[i]
	return l
