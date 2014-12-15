from sys import argv
import random
from numpy.random import rand

p = range(26)
random.shuffle(p)

output = open(argv[1], "w")

alpha = float(argv[2])

for fname in argv[3:]:
	f = open(fname, "r")

	for line in f.readlines():
		z = ''
		i = 0
		for ch in line.strip():
			try:
				x = ord(ch) - ord('a')
				if rand() < alpha and i > 0 and z[i-1] != '.':
					z += '.'
				else:
					z += chr(p[x] + ord('a'))
			except:
				print '{} unsupported'.format(ch)
			i += 1
		output.write(z)
		output.write('\n')

output.close()

for i in xrange(len(p)):
	print '{} -> {}'.format(chr(ord('a') + i), chr(ord('a') + p[i]))