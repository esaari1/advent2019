def output(state):
	idx = 1
	for y in range(5):
		for x in range(5):
			if state & idx:
				print '#',
			else:
				print '.',
			idx = idx << 1
		print


def posIdx(x, y):
	idx = 1 << (y * 5) + x
	return idx

def bugCount(state, x, y):
	count = 0
	if x > 0:
		idx = posIdx(x - 1, y)
		if state & idx:
			count += 1
	if x < 4:
		idx = posIdx(x + 1, y)
		if state & idx:
			count += 1

	if y > 0:
		idx = posIdx(x, y - 1)
		if state & idx:
			count += 1

	if y < 4:
		idx = posIdx(x, y + 1)
		if state & idx:
			count += 1
	return count

def cycle(state):
	newState = 0
	idx = 1
	for y in range(5):
		for x in range(5):
			count = bugCount(state, x, y)
			if count == 1 and (state & idx):
				newState = newState + idx
			if (not (state & idx)) and (count == 1 or count == 2):
				newState = newState + idx
			idx = idx << 1
	return newState

f = open('input.txt','r')
lines = f.readlines()
f.close()

state = 0

idx = 1

for line in lines:
	for c in line.strip():
		if c == '#':
			state = state + idx
		idx = idx << 1

states = {}
states[state] = True

while True:
	state = cycle(state)
	if state in states:
		output(state)
		print
		print state
		exit(0)
	states[state] = True
