start = 137683
end = 596253

i = start
count = 0

while i < end:
	s = str(i)
	inorder = True
	pair = False

	for idx in range(5):
		if s[idx] > s[idx+1]:
			inorder = False
			break

		if s[idx] == s[idx + 1]:
			pair = True

	if inorder and pair:
		count += 1

	i += 1

print count