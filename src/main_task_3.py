from metropolis import MetropolisPermutationGenerator
import quality
from multiprocessing import Pool


def get_lines(filename, lines_num=float('inf'), discard=0):
    lines = []
    cnt = 0
    with open(filename, 'r') as f:
        for line in f:
            cnt += 1
            if cnt <= discard:
                continue
            lines.append(line.rstrip())
            if cnt >= lines_num + discard:
                break

    return lines


def experiment(training_set_words):
    message = get_lines("../data/oliver_twist.txt", lines_num=8192, discard=5000)
    encrypted_message = get_lines("../data/encrypted.txt", lines_num=8192, discard=5000)
    perm_generator = MetropolisPermutationGenerator(print_info=False)
    perm_generator.set_encrypted_data(encrypted_message)
    perm_metropolis_fname = '../data/perm_metropolis_' + str(training_set_words) + '.txt'
    with open(perm_metropolis_fname, 'a') as f:
        print >>f, "Training set size: " + str(training_set_words)

    perm_generator.set_train_data(get_lines("../data/super.txt", lines_num=training_set_words))
    quality_results_array = []

    for j in xrange(0, 50):
        perm = perm_generator.generate_permutation(2500)
        q = quality.quality(encrypted_message, message, perm)
        quality_results_array.append(q)

        original = {value: key for key, value in perm.iteritems()}
        with open(perm_metropolis_fname, 'a') as f:
            for key in sorted(original.keys()):
                print >>f, key, "->", original[key]
            print >>f, q
            print >>f, ""

    to_print = str(training_set_words)
    to_print += ' ' + str(2500)
    for q in quality_results_array:
        to_print += ' ' + str(1.0-q)
    with open('../data/results_' + str(training_set_words) + '.txt', 'a') as f:
        print >>f, to_print


p = Pool(4)
training_set_words_list = [2**i for i in xrange(13, 26)]

p.map(experiment, training_set_words_list)
