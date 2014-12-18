import matplotlib.pyplot as plt

files_number = 4

for i in xrange(files_number):
    f = open("../../data/test_only_improvements_" + str(i + 1) + ".txt")
    lines = f.readlines()
    iter = []
    ll = []
    for line in lines:
        line = line.split()
        iter.append(int(line[0]))
        ll.append(float(line[-1]))
        print ll[-1], 
        print iter[-1]
        
        
    s = []
    for i in xrange(len(ll) - 1):
        s.append(ll[0])
        for j in xrange(i - 1):
            s[-1] += ll[j + 1]
        
        if i > 0:
            s[-1] /= i
    
    print len(s)
    print len(iter)
    plt.plot(iter[:-1], s)

plt.xlabel("iteration")
plt.ylabel("log-likelihood")
plt.show()