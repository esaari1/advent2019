xstart = 0
ystart = 3
size = 100

input = [109,424,203,1,21102,11,1,0,1105,1,282,21102,1,18,0,1106,0,259,2101,0,1,221,203,1,21102,1,31,0,1106,0,282,21102,38,1,0,1105,1,259,20101,0,23,2,22101,0,1,3,21101,1,0,1,21101,57,0,0,1105,1,303,2101,0,1,222,21001,221,0,3,21002,221,1,2,21101,0,259,1,21102,80,1,0,1106,0,225,21102,89,1,2,21102,91,1,0,1105,1,303,2101,0,1,223,20101,0,222,4,21101,0,259,3,21102,1,225,2,21102,225,1,1,21102,118,1,0,1106,0,225,20101,0,222,3,21101,136,0,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,1202,1,1,223,20102,1,221,4,21001,222,0,3,21102,18,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21101,214,0,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,21201,-3,0,1,22102,1,-2,2,21202,-1,1,3,21102,1,250,0,1105,1,225,21201,1,0,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21102,343,1,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,384,1,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0]
#input = [3,20,3,21,2,21,22,24,1,24,20,24,9,24,204,25,99,0,0,0,0,0,10,10,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1]

relativeBase = 0
debug = False
useX = True

delta = size - 1
result = -1

x = xstart
y = ystart


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

def processOutput(val):
	global result
	result = val


def handleInput(val, x, y):
	global useX

	if useX:
		input[val] = x
		useX = False
	else:
		useX = True
		input[val] = y

def doRun(x, y):
	global i, input, relativeBase, useX

	i = 0
	input = [109,424,203,1,21102,11,1,0,1105,1,282,21102,1,18,0,1106,0,259,2101,0,1,221,203,1,21102,1,31,0,1106,0,282,21102,38,1,0,1105,1,259,20101,0,23,2,22101,0,1,3,21101,1,0,1,21101,57,0,0,1105,1,303,2101,0,1,222,21001,221,0,3,21002,221,1,2,21101,0,259,1,21102,80,1,0,1106,0,225,21102,89,1,2,21102,91,1,0,1105,1,303,2101,0,1,223,20101,0,222,4,21101,0,259,3,21102,1,225,2,21102,225,1,1,21102,118,1,0,1106,0,225,20101,0,222,3,21101,136,0,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,1202,1,1,223,20102,1,221,4,21001,222,0,3,21102,18,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21101,214,0,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,21201,-3,0,1,22102,1,-2,2,21202,-1,1,3,21102,1,250,0,1105,1,225,21201,1,0,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21102,343,1,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,384,1,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0]
	relativeBase = 0
	useX = True

	while True:
		res = parseOpcode(input[i])

		if debug:
			print res, input[i]

		opcode = res[3]

		if opcode == 99:
			return

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
			handleInput(val, x, y)
			i += 2
			#exit(0)

		# print output
		elif opcode == 4:
			val = getVals1(i, res[0])
			processOutput(val)
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
			return

def process(xs, ys):
	x = xs
	y = ys
	while True:
		#upper left
		doRun(x, y)
		if result == 1:
			# upper right
			doRun(x + delta, y)
			if result == 1:
				#lower left
				doRun(x, y+delta)
				if result == 1:
					#lower right
					doRun(x+delta, y+delta)
					if result == 1:
						print x+1, y+1, 'DONE'
						print x * 10000 + y
						exit(0)

					else: #lower right
						lr = 1
						print 'WHAT?'
						exit(1)
				else: #lower left
					ll = 1
					x += 1
			else: #upper right
				y += 1
		else: #upper left
			x += 1


def processResult(x, y):
	if result == 1:
		print x, y, result
		oldx = x
		x = x + delta
		doRun(x, y)

		if result == 0:
			y += 1
			x = oldx
		else:
			print x, y, result
			exit(0)
	else:
		x += 1


if __name__ == "__main__":
	i = 0

#	x = int(sys.argv[1])
#	y = int(sys.argv[2])
	process(xstart, ystart)

