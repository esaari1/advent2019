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

steps = 1000

class Pos:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def same(self, o):
		return self.x == o.x and self.y == o.y and self.z == o.z

	def output(self):
		print self.x, self.y, self.z

	def energy(self):
		return abs(self.x) + abs(self.y) + abs(self.z)

class Vec:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def output(self):
		print self.x, self.y, self.z

	def energy(self):
		return abs(self.x) + abs(self.y) + abs(self.z)


class Planet:
	def __init__(self, vals):
		self.pos = Pos(vals[0], vals[1], vals[2])
		self.vel = Vec(0, 0, 0)

	def getUpdateVel(self, p, o):
		if p < o:
			return 1
		if p > o:
			return -1
		return 0

	def updateVel(self, o):
		self.vel.x += self.getUpdateVel(self.pos.x, o.x)
		self.vel.y += self.getUpdateVel(self.pos.y, o.y)
		self.vel.z += self.getUpdateVel(self.pos.z, o.z)

	def updatePos(self):
		self.pos.x += self.vel.x
		self.pos.y += self.vel.y
		self.pos.z += self.vel.z

	def potential(self):
		return self.pos.energy()

	def kinetic(self):
		return self.vel.energy()

	def hash(self):
		res = 7
		res = 31 * 7 + self.pos.x
		res = 31 * 7 + self.pos.y
		res = 31 * 7 + self.pos.z
		res = 31 * 7 + self.vel.x
		res = 31 * 7 + self.vel.y
		res = 31 * 7 + self.vel.z

planets = []
for i in input:
	planets.append(Planet(i))

for s in range(steps):
	for a in planets:
		for b in planets:
			if not a.pos.same(b.pos):
				a.updateVel(b.pos)

	for a in planets:
		a.updatePos()

energy = 0

for p in planets:
	energy += p.potential() * p.kinetic()
	
print energy