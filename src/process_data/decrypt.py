import sys


def decrypt(encrypted_file, decrypted_file, perm):
    '''
     perm[encoded letter] = decoded letter 
    '''
    p = {}
    with open(perm, 'r') as f:
        for l in f.readlines():
            p[l[2]] = l[0]
    f = open(encrypted_file, 'r')
    df = open(decrypted_file, 'w')
    
    for line in f.readlines():
        for ch in line.strip():
            try:
                df.write(p[ch])
            except:
                print '{} unsupported'.format(ch)
                df.write('\n')
        df.write('\n')
    f.close()
    df.close()

if __name__ == "__main__":
    decrypt(sys.argv[1], sys.argv[2], sys.argv[3])
