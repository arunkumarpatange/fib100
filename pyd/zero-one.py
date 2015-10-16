
def zero_one(n):

	def binary():
		k = 1
		while True:
			yield bin(k)
			k = k + 1

	for x in binary():
		if int(x[2:]) % n == 0:
			return int(x[2:])
	return 0


for n, _bin in (
	(4, 100),
	(5, 10),
	(6, 1110),
	(7, 1001),
	(13, 1001),
	(17, 11101),
	(225, 11111111100),
):
	assert zero_one(n) == _bin, zero_one(n)
