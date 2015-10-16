from pyd.helpers import get_tree


def bst_range(root, range):
	
	_min, _max = range

	def _bst(node):
		if node is None: return 0

		return (
			_bst(node.left) +
			_bst(node.right) +
			1 if node.val >= _min and node.val <= _max else 0
		)
	return _bst(root)

assert bst_range(get_tree(), (4, 10)) == 5
