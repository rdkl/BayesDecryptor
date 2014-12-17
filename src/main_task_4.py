from metropolis import MetropolisPermutationGenerator
from collections import Counter


test_msg = "_only_improvements_4"

#--------------------------------------------------------------------
permGenerator = MetropolisPermutationGenerator(print_info = False)
permGenerator.set_train_data()

f = open("../data/oliver_twist.txt", "r")
line_list = f.readlines()[0:12801]
permGenerator.set_encrypted_data(line_list)

unigram_counter = Counter()
unigram_number = 0.0

for line in line_list:
    line = line.strip()
    for word in line.split():
        if len(word) > 0:
            for i in xrange(len(word)):
                unigram_counter[word[i]] += 1.0
                unigram_number += 1.0
                
for key in unigram_counter.keys():
    unigram_counter[key] /= unigram_number
    
err_mean = 0
num_iter = 50

for i in xrange(num_iter):
    error = 0.0
    
    perm = permGenerator.generate_permutation(2500)
    for key in sorted(perm.keys()):
        print key, perm[key]
        
    with open('../data/perm_metropolis' + str(test_msg) + '.txt', 
              'w') as f:
          for key in sorted(perm.keys()):
              print >>f, key, perm[key]
              if key != perm[key]:
                  error += unigram_counter[key]
                          
    print error
    err_mean += error/num_iter

print err_mean