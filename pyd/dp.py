
def long_sub_palindromes(str):
	def _sub(str, i, j):
		if i == j:
			return 1

		if str[i] == str[j] and i + 1 == j:
			return 2

		if str[i] == str[j]:
			return 2 + _sub(str, i + 1, j - 1)
		return max(_sub(str, i + 1, j), _sub(str, i, j - 1))

	return _sub(str, 0, len(str) - 1)


assert long_sub_palindromes("abcdecba") == 7
