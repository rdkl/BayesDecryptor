import math
import string

from src.process_data.get_bigram_frequency import get_bigram_frequency


#-----------------------------------------------------------------------------
def get_letter_distribution(bigram_dist, previous_letter):
    dist = {letter : 0.0 for letter in string.lowercase}
    for key in dist:
        s = 0.0
        for letter in string.lowercase:
            s += bigram_dist[previous_letter + letter] * \
                bigram_dist[letter + key]
        dist[key] = s
        
    return dist

#-----------------------------------------------------------------------------
def estimate_log_likelihood(text, bigram_dist, perm, threshold=10**(-4),
                            missing_character="."):
    
    
    log_likelihood = 0.0

    for line in text:
        line = line.strip()
        for word in line.split():
            log_likelihood += math.log(bigram_dist["unigram"][word[0]])
            
            for i in xrange(1, len(word)):
                if word[i] == missing_character:
                    continue
                
                if word[i - 1] == missing_character:
                    dist = get_letter_distribution(bigram_dist, word[i - 2])
                    log_likelihood += math.log(max(dist[word[i]],
                                                   threshold))
                    continue
                
                bigram_probability = bigram_dist[perm[word[i - 1]] + \
                                                 perm[word[i]]]
                log_likelihood += math.log(max(bigram_probability, 
                                                threshold))
    return log_likelihood

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    print estimate_log_likelihood(["t."], 
                              get_bigram_frequency("../data/war_and_peace.txt"), 
                              {"a":"f", "b":"a", "f":"b"})
    
