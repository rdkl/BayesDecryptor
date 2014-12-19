from sys import argv
import random
from numpy.random import rand

def crypt_text(path="../../data/oliver_twist.txt", alpha=0.1):
	p = range(26)
	#random.shuffle(p)
	
	input = open(path, "r")
	
	output_list = []	
	for line in input.readlines():
		z = ''
		i = 0
		for ch in line.strip():
			try:
				x = ord(ch) - ord('a')
				if i > 0 and (z[-1] != '.') and rand() < alpha:
					z += '.'
				else:
					z += chr(p[x] + ord('a'))
			except:
				print '{} unsupported'.format(ch)
			i += 1
		output_list.append(z)
	
	return output_list
	
	#for i in xrange(len(p)):
	#	print '{} -> {}'.format(chr(ord('a') + i), chr(ord('a') + p[i]))
	
#-----------------------------------------------------------------------------

#print crypt_text()