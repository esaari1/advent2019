def matchLen(s, j):
	c = 1
	while j < 5:
		if s[j] == s[j + 1]:
			c += 1
		else:
			return c
		j += 1
	return c

def hasPair(s):
	idx = 0

	while idx < 5:
		l = matchLen(s, idx)
		if l == 2:
			return True
		idx += l
	return False

if __name__ == "__main__":
	start = 137683
	end = 596253

	i = start
	count = 0

	while i < end:
		s = str(i)
		inorder = True

		for idx in range(5):
			if s[idx] > s[idx+1]:
				inorder = False

		if inorder:
			if hasPair(s):
				count += 1

		i += 1

	print count
