import re
import time
import os
import string
from collections import Counter

starts = time.clock()


def s(s1, s2):
    if qu[s1] == seq2[s2]:
        return 2
    else:
        return -1



def alignment(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    g = -3
    matrix = []
    for i in range(0, m):
        tmp = []
        for j in range(0, n):
            tmp.append(0)
        matrix.append(tmp)
    for k in range(0, m):
        matrix[k][0] = k * g
    for h in range(0, n):
        matrix[0][h] = h * g
    for t in range(1, m):
        for f in range(1, n):
            matrix[t][f] = max(matrix[t - 1][f] + g, matrix[t - 1][f - 1] + s(t, f),
                                     matrix[t][f - 1] + g)
    a1 = [seq1[m - 1]]
    a2 = [seq2[n - 1]]
    while m > 1 and n > 1:
        if max(matrix[m - 1][n - 2], matrix[m - 2][n - 2], matrix[m - 2][n - 1]) == matrix[m - 2][n - 2]:
            m -= 1
            n -= 1
            a1.append(seq1[m - 1])
            a2.append(seq2[n - 1])
        elif max(matrix[m - 1][n - 2], matrix[m - 2][n - 2], matrix[m - 2][n - 1]) == matrix[m - 1][n - 2]:
            n -= 1
            a1.append('-')
            a2.append(seq2[n - 1])
        else:
            m -= 1
            a1.append(seq1[m - 1])
            a2.append('-')
    a1.reverse()
    a2.reverse()
    b1 = string.join(a1, '')
    b2 = string.join(a2, '')
    global score
    score = 0
    for k in range(0, len(b1)):
        if seque1[k] == seque2[k]:
            score += 1
    score = float(score)/len(b2)
    return b1, b2

def show(seq1,seq2):
    le = 40
    while len(seq1)-le>=0:
        print 'sequence1:',
        for code in list(seq1)[le-40:le]:
            print code,
        print "\n",
        print '          ',
        for gene in range(le-40, le):
            if seq1[gene]==seq2[gene]:
                print '|',
            else:
                print  ' ',
        print "\n",
        print 'sequence2:',
        for codes in list(seq2)[le-40:le]:
            print codes,
        print "\n",
        le +=40

    if len(seq1)>le-40:
        print 'sequence1:',
        for t in list(seq1)[le-40:len(seq1)]:
                print t,
        print "\n",
        print '          ',
        for dd in range(le-40, len(seq1)):
            if seq1[dd] == seq2[dd]:
                print '|',
            else:
                print ' ',
        print "\n",
        print 'sequence2:',
        for b in list(seq2)[le-40:len(seq2)]:
                print b,
        print "\n"
        
def inin(w):
    loc = dict()
    loc[w] = []
    if os.path.exists('/3_disk/wangcz/try3/lib2/library/'+w):
        word = open('/3_disk/wangcz/try3/lib2/library/'+w, 'r')
        for ii in range(1, 26):
            loc[w].append([])
        for line in word:
            if re.match(r"[\d]:(.*)", line):
                ch = line[0:1]
            elif re.match(r"[\d]{2}:(.*)", line):
                 ch = line[0:2]
            else:
                line = map(int, (line.split()))
                loc[w][int(ch)-1] = line
        word.close()
        return loc[w]
    else:
        for i in range(0, 25):
            loc[w].append([])
        return loc[w]


def chromosome(words):
    loc = dict()
    for w in words:
        loc[w] = inin(w)
    lenw = len(loc)
    global qu
    lenq = len(qu)
    qu_ = qu[0:6]
    qu__ = qu[-6:len(qu)]
    for j in range(0, 24):
        for u in range(0, lenw-1):
            for p in range(0, len(loc[words[u]][j])):
                loc[words[u]][j][p] += lenw-u-1
        chj = []
        for r in words:
            chj += loc[r][j]
        chjj = Counter(chj)
        local = []
        for chjj_ in chjj:
           if chjj[chjj_] > 5:
                local.append(chjj_)
        if local:
            chromo = open('/3_disk/wangcz/try2/chromosome/chromosome'+str(j+1)+".txt", 'r')
            chromoso = chromo.read().strip()
            for local_ in local:
                temp = chromoso[local_-lenq:local_+15]
                for ijk in range(0, lenq):
                    if temp[ijk:ijk+5].upper() in qu_:
                        break
                for ijkm in range(0, 15):
                    if temp[-5-ijkm:len(temp)-ijkm].upper() in qu__:
                        break
                global seq2
                seq2 = temp[ijk:len(temp)-ijkm].upper()
                (seque1, seque2) = alignment(qu, seq2)
                if score > 0.75:
                    print "find in chromosome"+str(j+1)
                    print str(local_-lenq+ijk)+' ---> '+str(local_+lenq-ijkm)
                    print temp[ijk:len(temp)-ijkm]+"\n"
                    show(seque1, seque2)
                    print "the score is "+str(score)+"\n"
            chromo.close()
        if not local:
            continue


qu = 'GTTGCAGACATGGTGTGTTGCTGGAGGAGACTGGGTCTGCTGCTTGAGGCCTTGTGAGCTGCAGGGGCACCCCCATGGGCAGGTGTGGCAGGTGAGTGCACACTGAGTCCTGAAGGGGCTGGCCTTCCGGGCTCCTTGGG'


i = 0
word = []
while i <= len(qu)-11:
    word.append(qu[i:i+11])
    i += 1

seq2 = ''
score = 0
chromosome(word)

end = time.clock()
print "using time: %fs" % (end - starts)



