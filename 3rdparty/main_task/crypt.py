from sys import argv
import random

def crypt(output_filename, input_filenames):
    p = range(26)
    random.shuffle(p)

    output = open(output_filename, "w")

    for fname in input_filenames:
        f = open(fname, "r")
        
        for line in f.readlines():
            for ch in line.strip():
                try:
                    x = ord(ch) - ord('a')
                    output.write(chr(p[x] + ord('a')))
                except:
                    print '{} unsupported'.format(ch)
                    output.write('\n')
            output.write('\n')
        f.close()    
    output.close()
    
    with open('../../data/perm.txt', 'w') as f:
        for i in xrange(len(p)):
            print >>f, chr(ord('a') + i), chr(ord('a') + p[i])

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    crypt(argv[1], argv[2:])
