from metropolis import MetropolisPermutationGenerator
from collections import Counter
import string
import numpy as np 

def quality(correct_perm, found_perm, unigram_counter):
    '''
    perm[encr] = decr
    '''
    error = 0.0
    for key in correct_perm:
        if correct_perm[key] != found_perm[key]:
            error += unigram_counter[key]
    return error
    
def get_unigramm_counter(text):
    unigram_counter = Counter()
    unigram_number = 0.0
    for line in text:
        line = line.strip()
        for word in line.split():
            if len(word) > 0:
                for i in xrange(len(word)):
                    unigram_counter[word[i]] += 1.0
                    unigram_number += 1.0
                    
    for key in unigram_counter.keys():
        unigram_counter[key] /= unigram_number
    return unigram_counter

f = open('../data/oliver_twist.txt')
text = f.readlines()
f.close()

permGenerator = MetropolisPermutationGenerator(print_info = False)
permGenerator.set_train_data()
correct_perm = {}
# with open('../data/perm.txt') as f:
#    for line in f.readlines():
#        correct_perm[line[2]] = line[0]
# print correct_perm

alph = string.ascii_lowercase
correct_perm = {i:i for i in alph}

num_iter = 50
words_error = {}
found_perm = {}
for number_of_words in xrange(10, 541, 40):
    unigram_counter = get_unigramm_counter(text[1000:1001 + number_of_words])
    permGenerator.set_encrypted_data(text[1000:1001+number_of_words])
    error = range(num_iter)
    print number_of_words
    
    for i in xrange(num_iter):
        found_perm[i] = permGenerator.generate_permutation(2500)
        error[i] = quality(correct_perm, found_perm[i], unigram_counter)
    words_error[number_of_words] = error
    print found_perm[np.argmin(error)], np.min(error), np.mean(error), np.var(error)
    
with open('../data/main_task_5_greedy_from1000.txt', 'w') as f:
    for key in sorted(words_error.keys()):
        print >>f, key, str(1), " ".join(map(str, words_error[key]))
# metropolis - 0
# greedy - 1
# 3 - result to use
# from1000 - start from 1000th word in text

