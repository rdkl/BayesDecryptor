from sys import argv
from collections import Counter

def get_bigram_frequency(input_filename):
    training = open(input_filename, "r")
    bigram_cnt = Counter()

    for line in training.readlines():
        strline = line.strip()
        for i in xrange(len(strline) - 1):
            bigram_cnt[strline[i] + strline[i + 1]] += 1.0
        
    bigram_number = sum(bigram_cnt.values())
    for key in bigram_cnt.keys():
        bigram_cnt[key] /= bigram_number
    return bigram_cnt

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print get_bigram_frequency("test.txt")
    