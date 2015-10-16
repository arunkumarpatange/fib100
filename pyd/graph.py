def depth(tree, _root, l_count=0, r_count=0):
	if tree.get(_root) is not None:
		left, right = tree[_root]
		if left == right == None: return 0, 0
		ll, lr, rl, rr = 0, 0, 0, 0
		if left is not None:
			ll, lr = depth(tree, left)
		if right is not None:
			rl, rr = depth(tree, right)
		return max(ll, lr, rl, rr) + 1, min(ll, lr, rl, rr) + 1

	#return max(l_count, r_count), min(l_count, r_count)
	return l_count, r_count

assert depth({1: (None, None)}, 1) == (0, 0)
assert depth({
	1: (2, 3),
}, 1) == (1, 1)

assert depth({
	1: (2, 3),
	2: (4, 5),
	3: (6, 7),
	4: (8, 9),
	6: (10, None),
	7: (11, None),
	10: (12, None),
	12: (13, None),
}, 1) == (5, 2)

def is_bst(tree, _root):
	# forces prev to be global in the closure
	prev = [None]

	def _is_bst(tree, _root):
		if tree.get(_root) is not None:
			left, right = tree.get(_root)
			x = _is_bst(tree, left)
			# print _root, prev
			if prev[0] > _root: return False
			prev[0] = _root
			y = _is_bst(tree, right)
			return x and y

		_prev = _root
		if prev[0] is not None:
			_prev = prev[0]

		# print _root, prev
		prev[0] = _root
		return _root >= _prev
	return _is_bst(tree, _root)
	
assert is_bst({}, 1)
assert is_bst({2: (1, 3)}, 2)
assert not is_bst({
	50: (30, 80),
	30: (20, 60),
	80: (70, 90),
}, 50)

def n_1th(tree, _root):
	''' n - 1th item '''
	if tree.get(_root) is not None:
		left, right = tree.get(_root)
		if tree.get(right) is not None:
			return n_1th(tree, right)
		#return nth(tree, right)
	return _root
assert n_1th({
	50: (30, 80),
	30: (20, 60),
	80: (70, 90),
}, 50) == 80

class Trie:

	@classmethod
	def prefixed(cls, strings):
		prev = ""
		trie = {}
		for str in strings:
			_trie = trie
			for s in str:
				_trie = _trie.setdefault(s, {})
		cls.data = trie
		return trie

	@classmethod
	def find(cls, str):
		_str = ""
		key = cls.data
		for c in str:
			key = key.get(c, None)
			if key is None:
				break
		else:
			return 'found'
		return 'not found'


print Trie.prefixed(["abcde", "abcf", 'az', 'ab', 'z'])
print Trie.find('abcdefg')
print Trie.find('ab')
print Trie.find('az')

from pyd.helpers import Bst as BstBase, get_tree
class Bst(BstBase):

	def _to_bst(self, in_order):
		index = [0]
		def _update(_root):

			if _root.left is not None:
				_left = _update(_root.left)

			_root.val = in_order[index[0]]
			index[0] = index[0] + 1

			if _root.right is not None:
				_right = _update(_root.right)

			return _root

		return _update(self._root)

	def flatten_bst(self):
		''' 
			traverse inorder and rebuild tree with first element as root
			a				b
		  /	  \		=> 		  \
		b       c				a
								 \
								   c
		'''
		in_order = []
		prev = [None]
		def _flatten(_root, path):
			left, right = _root.left, _root.right

			if left is not None:
				l_leaf = _flatten(left, path + '%s' % left.val)
			
			if left is None and right is None:
				print 'path %s' % path

			if prev[0] is None:
				prev[0] = _root.val
			if prev[0] <= _root.val:
				prev[0] = _root.val
			else:
				print 'is not bst'
			#print _root.val
			in_order.append(_root.val)

			if right is not None:
				r_leaf = _flatten(right, path + '%s' % right.val)
			# leaf
			return _root

		_flatten(self._root, '%s' % self._root.val)
		return in_order

	def in_order(self):
		l = []
		def _inorder(node):
			if node is None:
				return
			_inorder(node.left)
			l.append(node.val)
			_inorder(node.right)
	
		_inorder(self._root)
		return l

	def kth_smallest(self, k):

		k = [k]
		def _kth(node):
			if node is None:
				return 

			lval = _kth(node.left)

			if k[0] == 0:
				k[0] = -1
				return node.val
			k[0] = k[0] - 1

			rval = _kth(node.right)
			return lval or rval

		return _kth(self._root)

	def find_height(self):
		def _height(node):
			if node is None:
				return 0
			return 1 + max(_height(node.left), _height(node.right))
		def _min_height(node):
			if node is None:
				return 0
			return 1 + min(_height(node.left), _height(node.right))
		return _height(self._root), _min_height(self._root)

	def lca(self, a, b):
		'''
			common ancestor
		'''

		def _lca(node, a, b):
			if node is None:
				return

			if node.val == a or node.val == b:
				return node

			lnode = _lca(node.left, a, b)
			rnode = _lca(node.right, a, b)
			if lnode is not None and rnode is not None:
				return node

			return lnode or rnode

		return _lca(self._root, a, b).val

	def find(self, a, start=None):

		def _find(node, a, h=1, path=""):
			if node is None:
				return 0

			if node.val == a:
				print 'path %s%s' % (path,a)
				return h

			l = _find(node.left, a, h + 1, path + str(node.val))
			r = _find(node.right, a, h + 1, path + str(node.val))
			return l or r
		return _find(start or self._root, a)

	def find_sum(self, n):
		vals = []
		def _traverse(node, k):
			if node is None:
				return False

			for n in vals:
				if n + node.val == k:
					return (n, node.val)

			vals.append(node.val)
			return _traverse(node.left, k) or _traverse(node.right, k)
	
		return _traverse(self._root, n)

	def mirror(self):
		def _mirror(node):

			if node is None:
				return 

			_mirror(node.left)
			_mirror(node.right)

			node.left, node.right = node.right, node.left
		_mirror(self._root)
		return self

	def remove(self, val):
		'''
				1				2
			2		3	=>			3

		'''
		def _lefty(node):
			if node is None:
				return
	
			_node = _lefty(node.left)
			return _node or node

		def _del(node, val):
			if node is None:
				return 

			node.left = _del(node.left, val) 
			node.right = _del(node.right, val)
			if node.val == val:
				# delete node
				if node.left is None:
					return node.right
				if node.right is None:
					return node.left

				_node = _lefty(node.right)
				node.val = _node.val
				node.right = _del(node.right, node.val)
			return node
		root = _del(self._root, val)
		return self



bst = get_tree([4, 2, 0, 3, 5, 12], Bst)
assert bst.in_order() == [0, 2, 3, 4, 5, 12]
assert bst.flatten_bst() == [0, 2, 3, 4, 5, 12] # TODO: is wrong
bst._to_bst([1, 2, 3, 4, 5, 6])
bst.flatten_bst() # redo faltten bst
assert bst._root.val == 4

_bst = get_tree([3, 2, 1, 8, 9, 5, 4, 7], Bst)
assert _bst.find_height() == (4, 3)
assert _bst.kth_smallest(2) == 3
assert _bst.lca(2, 3) == 3
assert _bst.lca(1, 5) == 3
assert _bst.lca(4, 9) == 8
assert _bst.find(5) == 3
assert _bst.find_sum(6) == (1, 5)
assert _bst.mirror().in_order() == [9, 8, 7, 5, 4, 3, 2, 1]
assert _bst.mirror().in_order() == [1, 2, 3, 4, 5, 7, 8, 9]
assert _bst.remove(5).in_order()  == [1, 2, 3, 4, 7, 8, 9]
assert _bst.remove(3).in_order()  == [1, 2, 4, 7, 8, 9]
assert _bst._root.val == 4
assert _bst.remove(13).in_order()  == [1, 2, 4, 7, 8, 9]

_bst = get_tree([2, 1, 3], Bst)
assert _bst.remove(2).in_order() == [1, 3]
assert _bst._root.val == 3
