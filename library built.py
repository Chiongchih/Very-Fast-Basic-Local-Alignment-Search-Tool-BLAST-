import time
import re

starts = time.clock()

file = open("/3_disk/wangcz/try/harder/ch21.fasta", 'r')
lib = dict()
line = file.read().strip()
ii = 0
nii = 11
le = len(line)
while ii < le-11:
        M=line[ii]
        w = line[ii:ii+11]
        w = w.upper()
        if M=='N':
             nii+= 1
        elif lib.has_key(w):
             lib[w] += (" "+str(ii+nii-11))
             ii +=1
        else:
             lib[w] = str(ii+nii-11)
             ii += 1
for l in lib:
        fin = open('/3_disk/wangcz/try/harder/lib/chlib21', 'a')
        fin.write(str(l)+"\n")
        fin.write(lib[l]+"\n")
        fin.close()
file.close()

    

end = time.clock()
print "using time: %fs" % (end - starts)
