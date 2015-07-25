


def permutate(str):
	'''
		ab
		ba
	'''
	if len(str) <= 1:
		return [str]
	vals = permutate(str[1:])
	r = []
	for i in vals:
		for j in range(len(i) + 1):
			r.append(i[:j] + str[0] + i[j:])

	return r

