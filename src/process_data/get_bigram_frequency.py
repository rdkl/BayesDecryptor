from collections import Counter


def get_bigram_frequency(input_arg):
    # Output: conditional birgram distribution: p(a|b), normalized with 
    # respect to a. bigram_counter["unigram"] contains a distribution of first 
    # letters of words (in train text).
    
    if type(input_arg) != list and type(input_arg) != str:
        raise TypeError("Incorrect argument type, list or string expected, but"
                        "%s received" % str(type(input_arg)))          
    
    if type(input_arg) == list :
        train_text = input_arg
    else:
        f = open(input_arg, "r")
        train_text = f.readlines()
    
    bigram_counter = Counter()
    
    un_key = "unigram"    
    bigram_counter[un_key] = Counter()
    
    bigram_normilizer = Counter()
    
    for line in train_text:
        line = line.strip()
        for word in line.split():
            if len(word) > 0:
                # May be one-letter words should be rejected.
                bigram_counter[un_key][word[0]] += 1.0
       
            for i in xrange(len(word) - 1):
                bigram_counter[word[i:i + 2]] += 1.0
                bigram_normilizer[word[i + 1]] += 1.0
        
    unigram_number = sum(bigram_counter[un_key].values())
    
    for key in bigram_counter.keys():
        if key != un_key:
            bigram_counter[key] /= bigram_normilizer[key[0]]
    
    for key in bigram_counter[un_key]:
        bigram_counter[un_key][key] /= unigram_number
    
    if type(input_arg) == str:
        f.close()
        
    return bigram_counter

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    counter = get_bigram_frequency("../../data/war_and_peace.txt")
    for item in counter:
        print item, counter[item]
        