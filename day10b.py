import math
from collections import OrderedDict 

input = [
'.#..#',
'.....',
'#####',
'....#',
'...##']

input = [
'.#....#####...#..',
'##...##.#####..##',
'##...#...#.#####.',
'..#.....#...###..',
'..#.#.....#....##']

input = [
'.#..##.###...#######',
'##.############..##.',
'.#.######.########.#',
'.###.#######.####.#.',
'#####.##.#.##.###.##',
'..#####..#.#########',
'####################',
'#.####....###.#.#.##',
'##.#################',
'#####.##.###..####..',
'..######..##.#######',
'####.##.####...##..#',
'.#####..#.######.###',
'##...#.##########...',
'#.##########.#######',
'.####.#.###.###.#.##',
'....##.##.###..#####',
'.#.#.###########.###',
'#.#.#.#####.####.###',
'###.##.####.##.#..##']

input = [
'..#..###....#####....###........#',
'.##.##...#.#.......#......##....#',
'#..#..##.#..###...##....#......##',
'..####...#..##...####.#.......#.#',
'...#.#.....##...#.####.#.###.#..#',
'#..#..##.#.#.####.#.###.#.##.....',
'#.##...##.....##.#......#.....##.',
'.#..##.##.#..#....#...#...#...##.',
'.#..#.....###.#..##.###.##.......',
'.##...#..#####.#.#......####.....',
'..##.#.#.#.###..#...#.#..##.#....',
'.....#....#....##.####....#......',
'.#..##.#.........#..#......###..#',
'#.##....#.#..#.#....#.###...#....',
'.##...##..#.#.#...###..#.#.#..###',
'.#..##..##...##...#.#.#...#..#.#.',
'.#..#..##.##...###.##.#......#...',
'...#.....###.....#....#..#....#..',
'.#...###..#......#.##.#...#.####.',
'....#.##...##.#...#........#.#...',
'..#.##....#..#.......##.##.....#.',
'.#.#....###.#.#.#.#.#............',
'#....####.##....#..###.##.#.#..#.',
'......##....#.#.#...#...#..#.....',
'...#.#..####.##.#.........###..##',
'.......#....#.##.......#.#.###...',
'...#..#.#.........#...###......#.',
'.#.##.#.#.#.#........#.#.##..#...',
'.......#.##.#...........#..#.#...',
'.####....##..#..##.#.##.##..##...',
'.#.#..###.#..#...#....#.###.#..#.',
'............#...#...#.......#.#..',
'.........###.#.....#..##..#.##...']

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.length = math.sqrt(x*x + y*y)
		if self.length == 0:
			self.dot = 1
		else:
			self.dot = -self.y / self.length

		self.angle = math.acos(self.dot) * 180 / math.pi
		if self.x < 0:
			self.angle = 360 - self.angle

class Asteroid:
	dir = Vector(0, 0)
	slope = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def equal(self, other):
		return self.x == other.x and self.y == other.y

def sortKey(a, pos):
	dx = a.x - pos.x
	dy = a.y - pos.y
	dist = math.sqrt(dx * dx + dy * dy)
	return (a.dir.angle, dist)

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def delta(a, b):
	xd = abs(a.x - b.x)
	yd = abs(a.y - b.y)

	xm = 1
	ym = 1

	if a.x > b.x:
		xm = -1
	if a.y > b.y:
		ym = -1	

	if xd == 0 and yd == 0:
		return [0, 0]
	if xd == 0:
		return [0, ym]
	if yd == 0:
		return [xm, 0]

	g = gcd(xd, yd)
	return [xm * xd / g, ym * yd / g]

pos = Asteroid(11, 13)
pos = Asteroid(27, 19)

asteroids = []
for y in range(len(input)):
	line = input[y]

	for x in range(len(line)):
		if line[x] == '#':
			asteroids.append(Asteroid(x, y))
			
for a in asteroids:
	d = delta(pos, a)
	a.dir = Vector(d[0], d[1])

asteroids.sort(key = lambda a: sortKey(a, pos)) # a.dir.angle)

amap = OrderedDict()

for a in asteroids:
	if not a.equal(pos):
		if a.dir.angle not in amap:
			amap[a.dir.angle] = []
		amap[a.dir.angle].append(a)

for a in asteroids:
	if not a.equal(pos):
		print '[', a.x, a.y, ']', '[', a.dir.x, a.dir.y, ']', a.dir.angle

#for angle in amap:
#	print angle, len(amap[angle])

print 'ITEMS'
#for idx in range(len(amap.items())):
#	print amap.items()[idx][0]

#print amap.items()[0][1][0].x

print 'OUT'
idx = 0
for i in range(200):
	print amap.items()[idx][1][0].x, amap.items()[idx][1][0].y, amap.items()[idx][1][0].x * 100 + amap.items()[idx][1][0].y
	
	amap.items()[idx][1].pop(0)
	if len(amap.items()[idx][1]) == 0:
		amap.pop(amap.items()[idx][0])
	else:
		idx += 1
	if idx >= len(amap.items()):
		idx = 0
