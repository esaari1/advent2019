orig_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]

def attempt(noun, verb):
	input = orig_input[:]
	input[1] = noun
	input[2] = verb

	i = 0
	while True:
		opcode = input[i]
		idx1 = input[i + 1]
		idx2 = input[i + 2]
		idx3 = input[i + 3]

		if opcode == 99:
			break

		elif opcode == 1:
			input[idx3] = input[idx1] + input[idx2]

		elif opcode == 2:
			input[idx3] = input[idx1] * input[idx2]

		else:
			print 'bad ', opcode
			break

		i = i + 4

	return input[0]

if __name__ == "__main__":
	print 'main'

	for noun in range(0, 100):
		for verb in range(0, 100):
			result = attempt(noun, verb)
			if result == 19690720:
				print noun, verb, 100 * noun + verb
				exit(0)