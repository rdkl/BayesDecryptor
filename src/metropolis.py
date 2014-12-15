import random
import string

from estimate_likelihood import estimate_likelihood
from process_data.get_bigram_frequency import get_bigram_frequency


#-----------------------------------------------------------------------------
def get_start_permutation(text, bigram_distribution):
    likelihood = 0
    while likelihood == 0:
        letters_list = list(string.lowercase)
        random.shuffle(letters_list)
        letters = ''.join(letters_list)
        perm = dict(zip(string.lowercase, letters))
        likelihood = estimate_likelihood(train_file, bigram_distribution, 
                                         perm)
        
    return perm, likelihood
    
#-----------------------------------------------------------------------------
def get_next_permutation(perm):
    # Get two letters.
    (first, second) = random.sample(string.lowercase, 2)
    
    temp = perm[first]
    perm[first] = perm[second]
    perm[second] = temp
    
    return perm

#-----------------------------------------------------------------------------
def metropolis(perm, likelihood):
    
    candidate = get_next_permutation(perm)
    candidate_likelihood = estimate_likelihood(candidate)
    if candidate_likelihood == 0.0:
        return perm, likelihood
    
    candidate_probability = min(1, candidate_likelihood / likelihood)
    if candidate_probability > random.random():
        return candidate, candidate_likelihood
    
    return perm, likelihood

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    train_file = "../data/war_and_peace.txt"
    train_text = open(train_file, "r")
    train_bigram_distribuion = get_bigram_frequency(train_text) 
    
    start_perm = get_start_permutation(train_text, 
                                       train_bigram_distribuion)
    