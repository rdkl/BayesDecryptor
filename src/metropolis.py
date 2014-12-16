import copy
import math
import random
import string

from estimate_likelihood import estimate_likelihood
from estimate_log_likelihood import estimate_log_likelihood
from process_data.get_bigram_frequency import get_bigram_frequency


test_msg = "_only_improvements_4"

##############################################################################
class MetropolisPermutationGenerator(object):
    #-------------------------------------------------------------------------
    def __init__(self):
        self.__encrypted_text = []
        self.__train_bigram_dist = {}
        self.__test_file = open("../data/test"+ str(test_msg) + ".txt", "w")

    #-------------------------------------------------------------------------
    def set_train_data(self, train_file="../data/war_and_peace.txt"):
        if type(train_file) != list and type(train_file) != str:
            raise TypeError("Incorrect argument type, list or string expected"
                            ", but %s received" % (str(type(train_file))))
    
        if type(train_file) == str:
            train_text = open(train_file, "r").readlines()
        if type(train_file) == list:
            train_text = train_file
            
        self.__train_bigram_dist = get_bigram_frequency(train_text) 
        
    #-------------------------------------------------------------------------
    def set_encrypted_data(self, encrypted_file="../data/oliver_twist.txt"):
        if type(encrypted_file) != list and type(encrypted_file) != str:
            raise TypeError("Incorrect argument type, list or string expected"
                            ", but %s received" % (str(type(encrypted_file)))) 
    
        if type(encrypted_file) == str:
            self.__encrypted_text = open(encrypted_file, "r").readlines()
        if type(encrypted_file) == list:
            self.__encrypted_text = encrypted_file
            
    #-------------------------------------------------------------------------
    def __get_next_permutation(self, perm):
        # Get two letters.
        new_perm = copy.deepcopy(perm)
        (first, second) = random.sample(string.lowercase, 2)
        
        temp = new_perm[first]
        new_perm[first] = new_perm[second]
        new_perm[second] = temp
        
        return new_perm

    #-------------------------------------------------------------------------
    def __get_start_permutation(self):
        letters_list = list(string.lowercase)
        random.shuffle(letters_list)
        letters = ''.join(letters_list)
        perm = dict(zip(string.lowercase, letters))
        if self.__log_likelihood_flag:
            log_likelihood = estimate_log_likelihood(self.__encrypted_text, 
                                         self.__train_bigram_dist, perm)
            return perm, log_likelihood
        else:
            likelihood = estimate_likelihood(self.__encrypted_text, 
                                         self.__train_bigram_dist, perm)
            return perm, likelihood
            
    #-------------------------------------------------------------------------
    def __one_iteration_with_likelihood(self, perm, likelihood):
        
        candidate = self.__get_next_permutation(perm)
        candidate_likelihood = estimate_likelihood(self.__encrypted_text, 
                                                   self.__train_bigram_dist, 
                                                   candidate)
                
        # Probability is equal to one.
        if candidate_likelihood > likelihood:
            return candidate, candidate_likelihood
        
        candidate_probability = min(1, candidate_likelihood / likelihood)
        if candidate_probability > random.random():
            return candidate, candidate_likelihood
        
        return perm, likelihood
    
    #-------------------------------------------------------------------------
    def __one_iteration_with_log_likelihood(self, perm, log_likelihood):
        def print_candidate(candidate_log_l, log_l, candidate):
            out = "New ll = %.2f, " % candidate_log_l
            out += "old ll = %.2f, " % log_l
            out += "diff = %.2f\n" % (candidate_log_l - log_l)
            
            for key in string.lowercase:
                out += " " + key + ":" + candidate[key]
            
            print out + "\n"
        candidate = self.__get_next_permutation(perm)
        candidate_log_likelihood = estimate_log_likelihood(
                                                   self.__encrypted_text, 
                                                   self.__train_bigram_dist, 
                                                   candidate)
        
        # print >>self.__test_file, candidate_log_likelihood
        
        
        # Probability is equal to one.
        if candidate_log_likelihood > log_likelihood:
            print_candidate(candidate_log_likelihood, log_likelihood, 
                            candidate)
            return candidate, candidate_log_likelihood
        
        # Probability is equal to zero. Fixing overflow error.
        if candidate_log_likelihood < log_likelihood - 10000:
            return perm, log_likelihood
        
        
        candidate_probability = min(1, 
                    math.exp(candidate_log_likelihood - log_likelihood))
        if candidate_probability > random.random():
            print_candidate(candidate_log_likelihood, log_likelihood, 
                            candidate)
            return candidate, candidate_log_likelihood
        
        return perm, log_likelihood
    
    #-------------------------------------------------------------------------
    def generate_permutation(self, number_of_iterations, 
                             train_file=None, encrypted_file=None, 
                             use_log_likelihood = True):
        
        self.__log_likelihood_flag = use_log_likelihood
        
        if train_file is None and self.__train_bigram_dist == {}:
            raise ValueError("Train data wasn't set.")
        
        if encrypted_file is None and self.__encrypted_text == []:
            raise ValueError("Encrypted data wasn't set.")
        
        if use_log_likelihood:
            current_perm, current_log_likelihood = \
                self.__get_start_permutation()
            best_perm = current_perm
            best_log_likelihood = current_log_likelihood 
            
            for i in xrange(number_of_iterations):
                print >>self.__test_file, i,
                
                current_perm, current_log_likelihood = \
                    self.__one_iteration_with_log_likelihood(current_perm, 
                                         current_log_likelihood)
                
                # print current_perm
                # print current_log_likelihood
                if best_log_likelihood < current_log_likelihood:
                    best_perm = current_perm
                    best_log_likelihood = current_log_likelihood
                    print >>self.__test_file, i, best_log_likelihood

                if i % 100 == 0:
                    print "Iteration: ", i
                
            return best_perm
        else:
            current_perm, current_likelihood = \
                self.__get_start_permutation()
            best_perm = current_perm
            best_likelihood = current_likelihood
            
            for _ in xrange(number_of_iterations):
                current_perm, current_likelihood = \
                    self.__one_iteration_with_likelihood(current_perm, 
                                         current_likelihood)
                    
                print current_likelihood
                if best_likelihood < current_likelihood:
                    best_perm = current_perm
                    best_likelihood = current_likelihood
            
            return best_perm
    
    #-------------------------------------------------------------------------
##############################################################################
    
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    permGenerator = MetropolisPermutationGenerator()
    permGenerator.set_train_data()
    permGenerator.set_encrypted_data()
    
    perm = permGenerator.generate_permutation(2500)
    for key in sorted(perm.keys()):
        print key, perm[key]
        
    with open('../data/perm_metropolis' + str(test_msg) + '.txt', 
              'w') as f:
        for key in sorted(perm.keys()):
            print >>f, key, perm[key]
