input = [
	[-1, 0, 2],
	[2, -10, -7],
	[4, -8, 8],
	[3, 5, -1]
]

input = [
	[-8, -10, 0],
	[5, 5, 10],
	[2, -7, 3],
	[9, -8, -3]
]


input = [
	[-8, -9, -7],
	[-5, 2, -1],
	[11, 8, -14],
	[1, -4, -11]
]

def move(pos, vel):
	for idx in range(len(pos)):
		for idx2 in range(idx + 1, len(pos)):
			if pos[idx] < pos[idx2]:
				vel[idx] += 1
				vel[idx2] -= 1
			elif pos[idx] > pos[idx2]:
				vel[idx] -= 1
				vel[idx2] += 1

	for idx in range(len(pos)):
		pos[idx] += vel[idx]

def calculate(p, v):
	origP = p[:]
	origV = v[:]

	move(p,v)
	step = 1

	while p != origP or v != origV:
		move(p, v)
		step += 1

	return step

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


xp = []
yp = []
zp = []

xv = []
yv = []
zv = []

for i in input:
	xp.append(i[0])
	yp.append(i[1])
	zp.append(i[2])

	xv.append(0)
	yv.append(0)
	zv.append(0)

origXP = xp[:]
origXV = xv[:]

print 'x'
xstep = calculate(xp, xv)

print 'y'
ystep = calculate(yp, yv)

print 'z'
zstep = calculate(zp, zv)

print 'lcm'
print lcm(lcm(xstep, ystep), zstep)