import math

from process_data.get_bigram_frequency import get_bigram_frequency



def estimate_log_likelihood(text, bigram_dist, perm, threshold = 10**(-11)):
    '''
    perm is a dictionary: perm[encoded letter] = decoded letter
    '''    
    log_likelihood = 0.0

    for line in text:
        line = line.strip()
        for word in line.split():
            for i in xrange(len(word) - 1):
                bigram_probability = bigram_dist[perm[word[i]] + \
                                                 perm[word[i + 1]]]
                log_likelihood += math.log(max(bigram_probability, 
                                                threshold))
    
    return log_likelihood

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print estimate_log_likelihood(["bfbf aa"], 
                              get_bigram_frequency("../data/test.txt"), 
                              {"a":"f", "b":"a", "f":"b"})
    
