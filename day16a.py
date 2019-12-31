sin = '03036732577212944063491565474664'
phase = [0, 1, 0, -1]

sin = '123'

sin = sin * 10
print sin
exit(0)

loops = len(sin)

for j in range(100):
	newsin = ''
	for i in range(loops):
		cphase = []
		for p in phase:
			cphase.extend([p] * (i + 1))

		phaseIdx = 1
		val = 0
		for c in sin:
			i = int(c)
			val += i * cphase[phaseIdx]
			phaseIdx = (phaseIdx + 1) % len(cphase)
		newsin += str(val)[-1]

	sin = newsin
	print j+1, sin
print sin[:8]