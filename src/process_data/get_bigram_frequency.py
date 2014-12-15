from collections import Counter

def get_bigram_frequency(input_filename):
    training = open(input_filename, "r")
    bigram_counter = Counter()

    for line in training.readlines():
        line = line.strip()
        for word in line.split():
            for i in xrange(len(word) - 1):
                bigram_counter[word[i:i + 2]] += 1.0
        
    bigram_number = sum(bigram_counter.values())
    for key in bigram_counter.keys():
        bigram_counter[key] /= bigram_number
    return bigram_counter

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print get_bigram_frequency("../../data/test.txt")
    