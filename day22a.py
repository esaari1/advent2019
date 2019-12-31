count = 10007

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

cards = [x for x in range(count)]

print len(cards)

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
	#print cards

i = 0
while i < count:
	print i, cards[i]
	if cards[i] == 2019:
		print i
		exit(0)
	i += 1