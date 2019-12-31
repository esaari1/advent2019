count = 119315717514047

f = open('input.txt','r')
lines = f.readlines()
f.close()

def incrementDeal(cards, incr):
	c = 0
	idx = 0
	newcards = [0] * count
	while c < len(cards):
		newidx = idx % count
		if newcards[newidx] != 0:
			print 'BAD'
			exit(1)
		newcards[newidx] = cards[c]
		idx += incr
		c += 1
	return newcards

def cut(cards, amount):
	newcards = cards[amount:]
	newcards.extend(cards[0:amount])
	return newcards

cards = []
i = 0
while i < count:
	cards.append(i)

t = 0
while t < 101741582076661:
	print t, 101741582076661
	for l in lines:
		l = l.strip()
		print l
		if l[:19] == 'deal with increment':
			incr = int(l[20:])
			cards = incrementDeal(cards, incr)
		elif l == 'deal into new stack':
			cards = cards[::-1]
		elif l[:3] == 'cut':
			amount = int(l[4:])
			cards = cut(cards, amount)
		else:
			print l
			exit(1)
	t += 1

print cards[2020]
