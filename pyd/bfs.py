from pyd.datastructure import Node
from Queue import Queue

class Bfs(object):

	@classmethod
	def bfs(cls, queue):
		if queue.qsize() != 0:
			
			node, level = queue.get()
			print node.val, level
			yield node.val, level

			if node.left is not None:
				queue.put((node.left, level + 1))
			if node.right is not None:
				queue.put((node.right, level + 1))

			for v in cls.bfs(queue):
				yield v

	@classmethod
	def bfs_recur(cls, root):
		q = Queue()
		q.put((root, 0))

		return cls.bfs(q)


if "__main__" == __name__:
	'''
		 7
	  /     \
	5        6
  /   \     /  \
1      2   3    4
	'''

	leaf1 = Node(1)
	leaf2 = Node(2)
	leaf3 = Node(3)
	leaf4 = Node(4)

	node1 = Node(5, leaf1, leaf2)
	node2 = Node(6, leaf3, leaf4)
	root = Node(7, node1, node2)

	assert list(Bfs.bfs_recur(root)) == [
		(7, 0),
		(5, 1),
		(6, 1),
		(1, 2),
		(2, 2),
		(3, 2),
		(4, 2),
	]
