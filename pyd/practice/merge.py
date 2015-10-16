import heapq

def merge(*iters):

	heap = []
	iters = map(iter, iters)
	while True:
		for _iter in iters:
			v = next(_iter, None)
			if v is not None:
				heapq.heappush(heap, v)
		else:
			try:
				yield heapq.heappop(heap)
			except:
				break


assert list(merge(xrange(5, 10), xrange(1, 5), range(-5, 1))) == range(-5, 10)
