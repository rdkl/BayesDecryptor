import math

from process_data.get_bigram_frequency import get_bigram_frequency

#-----------------------------------------------------------------------------
def estimate_likelihood_words(text, bigram_dist, perm):
    '''
    perm is a dictionary: perm[encoded letter] = decoded letter
    '''    
    likelihood = 10**-10
    number_of_words = 0.0

    for line in text:
        line = line.strip()
        for word in line.split():
            number_of_words += 1
            
            word_likelihood = 1.0
            for i in xrange(len(word) - 1):
                bigram_probability = bigram_dist[perm[word[i]] + \
                                                 perm[word[i + 1]]]
                
                word_likelihood *= bigram_probability
                
            likelihood += word_likelihood
    
    return likelihood / number_of_words

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print estimate_likelihood(["bfbf aa"], 
                              get_bigram_frequency("../data/test.txt"), 
                              {"a":"f", "b":"a", "f":"b"})
    
