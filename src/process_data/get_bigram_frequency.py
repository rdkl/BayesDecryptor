from collections import Counter

def get_bigram_frequency(input_arg):
    if type(input_arg) != list and type(input_arg) != str:
        raise TypeError("Incorrect argument type, list or string expected, but"
                        "%s received" % str(type(input_arg)))          
    
    if type(input_arg) == list :
<<<<<<< HEAD
        train_text = input_arg
    else:
=======
        training = input_arg
    else
>>>>>>> a807d2f3c6a430af5882285faa974c09f3848235
        f = open(input_arg, "r")
        train_text = f.readlines()
        
    bigram_counter = Counter()

    for line in train_text:
        line = line.strip()
        for word in line.split():
            for i in xrange(len(word) - 1):
                bigram_counter[word[i:i + 2]] += 1.0
        
    bigram_number = sum(bigram_counter.values())
    for key in bigram_counter.keys():
        bigram_counter[key] /= bigram_number
    
    if type(input_arg) == str:
        f.close()
        
    return bigram_counter

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print get_bigram_frequency("../../data/test.txt")
    
