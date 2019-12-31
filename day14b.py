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
extra = {}

def requisition(amount, name):
	global required, extra

	if name == 'ORE':
		required += amount
		return

	req = amount - extra.get(name, 0)
	if req > 0:
		reaction = reactions[name]
		m = int(math.ceil(float(req) / float(reaction.result.amount)))

		for input in reaction.inputs:
			requisition(input.amount * m, input.name)

		extra[name] = extra.get(name, 0) + m * reaction.result.amount

	extra[name] -= amount


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

ONE_TRILLION = 1000000000000
print ONE_TRILLION

input = 1766154

requisition(input, "FUEL")
print required
