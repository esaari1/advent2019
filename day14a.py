import math

class Material:
	def __init__(self, c):
		self.amount, self.name = c.strip().split(' ')
		self.amount = int(self.amount)

class Reaction:
	def __init__(self, result, inputs):
		self.result = result
		self.inputs = inputs

required = 0
rem = {}

def requisition(amount, name):
	global required, rem

	if name == 'ORE':
		required += amount
		return

	req = amount - rem.get(name, 0)
	if req > 0:
		reaction = reactions[name]
		m = int(math.ceil(float(req) / float(reaction.result.amount)))

		for input in reaction.inputs:
			requisition(input.amount * m, input.name)

		rem[name] = rem.get(name, 0) + m * reaction.result.amount

	rem[name] -= amount


f = open('input.txt', 'r')
input = f.readlines()
f.close()

reactions = {}

for i in input:
	inout = i.strip().split('=>')
	result = Material(inout[1])

	inputs = []
	ins = inout[0].split(',')

	for val in ins:
		inputs.append(Material(val))

	reactions[result.name] = Reaction(result, inputs)

requisition(1, "FUEL")
print required
