

def max_set_bit(binary):
	binary = str(binary)

	ones = 0
	curr_flip_1, to_flips = 0, 0
	diff, max_diff = 0, 0
	start, end, cur_start = 0, 0, 0

	for i, b in enumerate(binary):
		if b == '1':
			ones = ones + 1
			diff = diff + 1
			curr_flip_1 = curr_flip_1 + 1
		else:
			diff = diff - 1

		if diff < max_diff:
			max_diff = diff
			start = cur_start
			end = i
			to_flips = curr_flip_1
		elif diff > 0:
			cur_start = i + 1
			diff = 0
			curr_flip_1 = 0

	# print end , start, to_flips , ones , to_flips
	return end - start + 1 - to_flips + ones - to_flips

assert max_set_bit(11111) == 6, 11111
assert max_set_bit(10010010) == 6, 11101110
assert max_set_bit(100100111101) == 10, 111011111101


def max_sub_array(A):

	cur_max = 0
	_max = 0

	for n in A:
		cur_max = max(0, cur_max + n)
		_max = max(_max, cur_max)
	# print _max
	return _max

assert max_sub_array([-1, 1, 1, -1, 1, 1, -1, 1]) == 3, '10010010 => [-1, 1, 1, -1, 1, 1, -1, 1]'


def max_bit_set(binary):

	_max, cur_max = 0, 0
	ones = 0
	for i, b in enumerate(str(binary)):
		if b == '0':
			n = 1
		else:
			ones = ones + 1
			n = -1

		if cur_max + n > 0:
			cur_max = cur_max + n
		else:
			cur_max = 0

		if _max < cur_max:
			_max = cur_max

	print ones , _max
	return ones + _max

assert max_bit_set(10010010) == 6, 11101110
assert max_bit_set(100100111101) == 10, 111011111101
