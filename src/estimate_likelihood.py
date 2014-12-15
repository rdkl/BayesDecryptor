from process_data.get_bigram_frequency import get_bigram_frequency

def estimate_likelihood(text, bigram_cnt, perm):
    '''
    perm is a dictionary: perm[encoded letter] = decoded letter
    '''    
    likelihood = 1.0

    for line in text:
        line = line.strip()
        for word in line.split():
            for i in xrange(len(word) - 1):
                likelihood *= bigram_cnt[perm[word[i]] + perm[word[i + 1]]]
        
    return likelihood

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print estimate_likelihood(["bfbf aa"], 
                              get_bigram_frequency("../data/test.txt"), 
                              {"a":"f", "b":"a", "f":"b"})
    
