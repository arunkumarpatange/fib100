
import unittest
from pyd.permutations import *



class PyTest(unittest.TestCase):

	def test_permuation(self):
		str = "abc"
		self.assertEqual({s for s in permutate(str)},
				{"abc","acb","bac", "bca", "cab", "cba"})

if __name__ == '__main__':
	unittest.main()
