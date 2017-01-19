import re
import time

starts = time.clock()
gene = open("/home/wangcz/blast/pgw.fa")

i = 0
for line in gene:
    if re.match(r">(.*)", line):
        if i > 0:
            fin = open("/home/wangcz/blast/chromosome/chromosome'+str(i)+'.txt', 'w')
            chrom = re.sub(r'\n', '', chrom)
            fin.write(chrom)
            fin.close()
        i += 1
        chrom = ''
    else:
        chrom += line

fin = open('/home/wangcz/blast/chromosome/chromosome'+str(i)+'.txt', 'w')
chrom = re.sub(r'\n', '', chrom)
fin.write(chrom)
fin.close()

gene.close()

end = time.clock()
print ("using time: %fs" % (end - starts))