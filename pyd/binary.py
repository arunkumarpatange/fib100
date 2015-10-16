from pyd.helpers import Bst as BstBase, get_tree, randomize


class Bst(BstBase):

	def max_sum_path(self):

		def _sum(node, val):
			if node is None:
				return val
			return max(_sum(node.left, node.val + val), _sum(node.right, node.val + val))

		return _sum(self._root, 0)

	def in_order(self):

		l = []
		def _order(node):

			if node is None: return l

			_order(node.left)
			l.append(node)
			_order(node.right)
			return l
		return _order(self._root)

	def _delete(self):
		def _d(root):
			q = [root]
			while len(q) != 0:
				node = q[0]
				q.remove(node)
				if node is not None:
					q.append(node.left)
					q.append(node.right)
					del node
		_d(self._root)
		self._root = None
		return self


bst = get_tree([4, 2, 0, 3, 5, 12], Bst)
assert bst.max_sum_path() == 21
assert map(lambda n: n.val, bst.in_order()) == [0, 2, 3, 4, 5, 12]
bst = get_tree(randomize(range(100000)), Bst)

assert bst._delete().in_order() == []
