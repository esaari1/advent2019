input = [3,8,1005,8,304,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,29,2,103,1,10,1,106,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,59,2,102,3,10,2,1101,12,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,88,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,110,2,108,9,10,1006,0,56,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,139,1,108,20,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,165,1,104,9,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,192,2,9,14,10,2,1103,5,10,1,1108,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,226,1006,0,73,1006,0,20,1,1106,11,10,1,1105,7,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,261,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,283,101,1,9,9,1007,9,1052,10,1005,10,15,99,109,626,104,0,104,1,21101,48062899092,0,1,21101,0,321,0,1105,1,425,21101,936995300108,0,1,21101,0,332,0,1106,0,425,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209382902951,1,1,21101,379,0,0,1106,0,425,21102,179544747200,1,1,21102,390,1,0,1106,0,425,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,709488292628,1,21102,1,413,0,1106,0,425,21101,0,983929868648,1,21101,424,0,0,1105,1,425,99,109,2,22101,0,-1,1,21102,40,1,2,21102,456,1,3,21101,446,0,0,1106,0,489,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,451,452,467,4,0,1001,451,1,451,108,4,451,10,1006,10,483,1102,0,1,451,109,-2,2105,1,0,0,109,4,1201,-1,0,488,1207,-3,0,10,1006,10,506,21102,1,0,-3,21202,-3,1,1,21201,-2,0,2,21101,0,1,3,21101,525,0,0,1105,1,530,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,553,2207,-4,-2,10,1006,10,553,21202,-4,1,-4,1105,1,621,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,572,0,1106,0,530,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,591,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,613,22101,0,-1,1,21101,0,613,0,106,0,488,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

relativeBase = 0

position = [0,0]

# 0 = up
# 1 = right
# 2 = down
# 3 = left
direction = 0
panels = {}

inputVal = 1

outputType = 0

debug = False

minX = None
minY = None
maxX = 0
maxY = 0

def turnAndMove(val):
	global direction
	global minX, maxX, minY, maxY

	if val == 0:
		direction -= 1
	else:
		direction += 1
	
	if direction < 0:
		direction = 3
	elif direction > 3:
		direction = 0

	if direction == 0:
		position[1] += 1
	elif direction == 1:
		position[0] += 1
	elif direction == 2:
		position[1] -= 1
	elif direction == 3:
		position[0] -= 1
	else:
		print 'bad direction ', direction
		exit(1)

	if minX is None or minX > position[0]:
		minX = position[0]
	if maxX < position[0]:
		maxX = position[0]

	if minY is None or minY > position[1]:
		minY = position[1]
	if maxY < position[1]:
		maxY = position[1]

def parseOpcode(o):
	s = str(o)
	while len(s) < 5:
		s = "0" + s
	return int(s[2]), int(s[1]), int(s[0]), int(s[3:])

def adjustLength(idx):
	clen = len(input)
	if clen <= idx:
		input.extend([0] * (idx - clen + 1))

def getVals(i, m1, m2, m3):
	val1, val2 = getVals2(i, m1, m2)
	val3 = input[i + 3]
	if m3 == 2:
		val3 += relativeBase
	return val1, val2, val3

def getVals2(i, m1, m2):
	val1 = getVals1(i, m1)
	val2 = input[i + 2]

	if m2 == 0:
		adjustLength(val2)
		val2 = input[val2]
	elif m2 == 2:
		adjustLength(val2 + relativeBase)
		val2 = input[val2 + relativeBase]

	return val1, val2

def getVals1(i, m1):
	val1 = input[i + 1]

	if m1 == 0:
		adjustLength(val1)
		val1 = input[val1]
	elif m1 == 2:
		adjustLength(val1 + relativeBase)
		val1 = input[val1 + relativeBase]

	return val1

if __name__ == "__main__":
	i = 0

	while True:
		res = parseOpcode(input[i])

		if debug:
			print res, input[i]

		opcode = res[3]

		if opcode == 99:
			break

		# add args
		elif opcode == 1:
			val1, val2, val3 = getVals(i, res[0], res[1], res[2])
			adjustLength(val3)
			if debug:
				print 'input[', val3, '] = ', val1, ' + ', val2
			input[val3] = val1 + val2
			i = i + 4

		# multiply args
		elif opcode == 2:
			val1, val2, val3 = getVals(i, res[0], res[1], res[2])
			adjustLength(val3)
			if debug:
				print 'input[', val3, '] = ', val1, ' * ', val2
			input[val3] = val1 * val2
			i = i + 4

		# get input
		elif opcode == 3:
			val = input[i + 1]
			if res[0] == 2:
				val = val + relativeBase
			adjustLength(val)
			if debug:
				print 'input[', val, '] = ', inputVal

			p = position[0] * 100 + position[1]
			if p in panels:
				input[val] = panels[p]
			else:
				input[val] = inputVal
				inputVal = 0
			i += 2

		# print output
		elif opcode == 4:
			val = getVals1(i, res[0])
			#print '4: ', val
			if outputType == 0:
				p = position[0] * 100 + position[1]
				panels[p] = val
				outputType = 1
			else:
				turnAndMove(val)
				outputType = 0
			i += 2

		# jump if not 0
		elif opcode == 5:
			val1, val2 = getVals2(i, res[0], res[1])
			if val1 != 0:
				i = val2
			else:
				i += 3

		# jump if 0
		elif opcode == 6:
			val1, val2 = getVals2(i, res[0], res[1])
			if val1 == 0:
				i = val2
			else:
				i += 3

		# check if less
		elif opcode == 7:
			val1, val2, val3 = getVals(i, res[0], res[1], res[2])
			adjustLength(val3)
			if val1 < val2:
				input[val3] = 1
			else:
				input[val3] = 0
			i += 4

		# check if equal
		elif opcode == 8:
			val1, val2, val3 = getVals(i, res[0], res[1], res[2])
			adjustLength(val3)

			if debug:
				print 'input[', val3, '] = ', val1, ' == ', val2

			if val1 == val2:
				input[val3] = 1
			else:
				input[val3] = 0
			i += 4

		# modify relative base
		elif opcode == 9:
			val1 = getVals1(i, res[0])
			relativeBase += val1
			i += 2

		else:
			print 'bad ', opcode
			break

	print len(panels)
	print minX, maxX, minY, maxY

	for y in range(maxY, minY - 1, -1): # range(minY, maxY + 1):
		for x in range(minX, maxX + 1):
			p = x * 100 + y
			if p in panels:
				if panels[p] == 1:
					print '1',
				else:
					print ' ',
			else:
				print ' ',
		print ''