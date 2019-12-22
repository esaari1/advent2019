ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = ALPHABET.lower()

none = -1
north = 0
east = 1
south = 2
west = 3

startNode = None
nodes = {}

# maps key name to its node, (key['a'] = node)
keyMap = {}


class Tree:
	def __init__(self, node, length = 0):
		self.node = node
		self.length = length
		self.keys = {}

	def addChild(self, node, length):
		n = Tree(node, self.length + length)
		n.keys = self.keys.copy()
		n.keys[node.key] = True
		return n

	def output(self):
		k = self.keys.keys()
		k.sort()
		print self.node.key, self.length, k, len(k)


class Path:
	def __init__(self, start, end, length, doors):
		self.start = start
		self.end = end
		self.length = length
		self.doors = doors

	def output(self):
		print self.start.key, self.end.key, self.length, self.doors

	def reverse(self):
		return Path(self.end, self.start, self.length, self.doors)

	def canDo(self, keys):
		# keys is list of all keys we have collected

		# Check that we have a key for all doors on the path
		for door in self.doors:
			if door not in keys:
				return False
		return True

class Node:
	def __init__(self, x, y, d):
		self.x = x
		self.y = y
		self.edges = [None, None, None, None]
		self.lastTry = none

		if d in ALPHABET:
			self.door = d.lower()
		else:
			self.door = None

		if d in alphabet:
			self.key = d
		else:
			self.key = None

	def link(self, other, dir):
		self.edges[dir] = other
		other.edges[(dir + 2) % 4] = self

	def positionHash(self, dir):
		x = self.x
		y = self.y

		if dir == north:
			y -= 1
		if dir == east:
			x += 1
		if dir == south:
			y += 1
		if dir == west:
			x -= 1
		return str(x) + '_' + str(y)

	def move(self, visited, nodeStack, doors, doorBlocks):
		while self.lastTry != 4:
			self.lastTry += 1
			if self.lastTry == 4:
				break

			if self.edges[self.lastTry] is None:
				continue

			hash = self.positionHash(self.lastTry)
			if hash not in visited:
				visited[hash] = True
				if nodes[hash].door is not None:
					if doorBlocks:
						continue
					doors[nodes[hash].door] = True
				nodeStack.append(self)

				return nodes[hash]

		if len(nodeStack) == 0:
			#print 'DONE'
			#exit(0)
			return None

		if self.door is not None and self.door in doors:
			del doors[self.door]

		return nodeStack.pop()


def findAllKeyPaths():
	paths = {}

	kkeys = keyMap.keys()
	a = 0
	while a < len(kkeys) - 1:
		b = a + 1
		while b < len(kkeys):
			path = findPath(keyMap[kkeys[a]], keyMap[kkeys[b]])

			if kkeys[a] not in paths:
				paths[kkeys[a]] = []
			paths[kkeys[a]].append(path)

			if kkeys[b] not in paths:
				paths[kkeys[b]] = []
			paths[kkeys[b]].append(path.reverse())
			b += 1
		a += 1

	return paths

def findPath(start, end, doorBlocks = False):
	for k in nodes:
		nodes[k].lastTry = none

	visited = {}
	nodeStack = []
	doors = {}
	n = start
	visited[n.positionHash(none)] = True

	while n.positionHash(none) != end.positionHash(none):
		n = n.move(visited, nodeStack, doors, doorBlocks)
		if n is None:
			return None
	path = Path(start, end, len(nodeStack), doors.keys())
	return path


def getPossibleKeys(node):
	paths = []
	for k in keyMap:
		if k != node.key:
			path = findPath(node, keyMap[k], True)
			if path:
				paths.append(path)
	return paths

min = 100000000
cache = {}

def cacheKey(loc, pastKeys):
	k = pastKeys.keys()
	k.sort()
	s = loc + '_' + '_'.join(k)
	return s


# return min distance to end or -1 for bad path
def buildTree(root, lvl = 0):
	global min, cache

	node = root.node
	#print 'ROOT', lvl, root.node.key, root.keys
	if lvl == maxRecurs:
		# reached the last key. 
		if min > root.length:
			print 'MIN = ', root.length
			min = root.length

	for path in keyPaths[node.key]:
		if root.length + path.length < min: # is new path less than current min
			if path.end.key not in root.keys: # have we already visited the path end on this run
				if path.canDo(root.keys): # do we have keys for all doors on path
					#print 'ADD CHILD', path.end.key
					child = root.addChild(path.end, path.length) # create tree node 
					buildTree(child, lvl + 1) # get distance from new node to end

# read input
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

data = []

for line in lines:
	line = line.strip()
	data.append(list(line))

# build graph
for y in range(1,len(data) - 1):
	line = data[y]
	for x in range(1, len(line) - 1):
		d = line[x]
		if d != '#':
			n = Node(x, y, d)
			nodes[n.positionHash(none)] = n
			if n.positionHash(north) in nodes:
				n.link(nodes[n.positionHash(north)], north)
			if n.positionHash(west) in nodes:
				n.link(nodes[n.positionHash(west)], west)

			if d == '@':
				startNode = n
				startNode.key = '@'
			elif d in alphabet:
				keyMap[d] = n

# Find all paths between keys
keyPaths = findAllKeyPaths()
maxRecurs = len(keyPaths)
print maxRecurs

# Find all keys reachable from start
startPaths = getPossibleKeys(startNode)
keyPaths['@'] = startPaths

if False:
	print len(keyPaths)
	for k in keyPaths:
		print k, len(keyPaths[k])
		keyPaths[k][0].output()

root = Tree(startNode)
buildTree(root)

print 'ANSWER', min
