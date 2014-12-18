from metropolis import MetropolisPermutationGenerator
from collections import Counter


test_msg = "_only_improvements_4"

#--------------------------------------------------------------------
permGenerator = MetropolisPermutationGenerator(print_info = False)
permGenerator.set_train_data()

size = 25600

f = open("../data/oliver_twist.txt", "r")
line_list = f.readlines()[0:size+1]
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
    
err_mean = 0.0
num_restarts = 50
num_iter = 2500

error = []

for i in xrange(num_restarts):
    error += [0.0]
    
    perm = permGenerator.generate_permutation(num_iter)
    #for key in sorted(perm.keys()):
        #print key, perm[key]
        
    for key in sorted(perm.keys()):
        if key != perm[key]:
            error[i] += unigram_counter[key]
            
    err_mean += error[i]/num_restarts
    print error[i]
                
with open('../data/main_task_4.txt', 'a') as g:
    print >>g, size, num_iter, " ".join(map(str, error))

g.close()
f.close()

print err_mean