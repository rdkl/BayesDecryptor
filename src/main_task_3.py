from metropolis import MetropolisPermutationGenerator
import quality


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

message = get_lines("../data/oliver_twist.txt", lines_num=8192, discard=5000)
encrypted_message = get_lines("../data/encrypted.txt", lines_num=8192, discard=5000)
permGenerator = MetropolisPermutationGenerator(print_info=False)
permGenerator.set_encrypted_data(encrypted_message)

training_set_words_list = [262144*1.5]
for training_set_words in training_set_words_list:
    with open('../data/perm_metropolis.txt', 'a') as f:
        print >>f, "Training set size: " + str(training_set_words)

    permGenerator.set_train_data(get_lines("../data/super.txt", lines_num=training_set_words))
    quality_results_array = []
    for j in xrange(0, 50):
        perm = permGenerator.generate_permutation(2500)
        q = quality.quality(encrypted_message, message, perm)
        quality_results_array.append(q)

        original = {value: key for key, value in perm.iteritems()}
        with open('../data/perm_metropolis.txt', 'a') as f:
            for key in sorted(original.keys()):
                print >>f, key, "->", original[key]
            print >>f, q
            print >>f, ""

    to_print = str(training_set_words)
    average = 0.0
    to_print += ' ' + str(2500)
    for q in quality_results_array:
        to_print += ' ' + str(1.0-q)
        average += q
    with open('../data/results.txt', 'a') as f:
        print >>f, to_print
    with open('../data/perm_metropolis.txt', 'a') as f:
        print "Average quality:", average
    training_set_words *= 2
