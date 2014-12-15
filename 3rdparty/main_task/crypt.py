from sys import argv
import random
from numpy.random import rand

p = range(26)
random.shuffle(p)

output = open(argv[1], "w")

for fname in argv[2:]:
	f = open(fname, "r")

	for line in f.readlines():
		for ch in line.strip():
			try:
				x = ord(ch) - ord('a')
				output.write(chr(p[x] + ord('a')))
			except:
				print '{} unsupported'.format(ch)
		output.write('\n')

output.close()

for i in xrange(len(p)):
	print '{} -> {}'.format(chr(ord('a') + i), chr(ord('a') + p[i]))