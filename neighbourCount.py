#FOR SHELL USE : python nieghbourCount.py file "kmer"
#HELP : python neighbourCount.py -h

import sys, argparse
from biopack import formatFasta, hammDist

#Help documentation
parser = argparse.ArgumentParser(
    description='Return the number of times a kmer appears in a sequence. Non-exact matches are allowed wihtin a neighbourhood of Hamming distance >= dist. Kmers cannot overlap.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('fasta', type=str, default='', help='FILE')
parser.add_argument('kmer', type=str, default='', help='"KMER"')
parser.add_argument('dist', type=int, default=0, help='HAMMING DIST')
args = parser.parse_args()

def neighbourCount(sequence, kmer, dist):
    '''Return the number of times a kmer appears in a sequence. Non-exact matches are allowed wihtin a neighbourhood of Hamming distance >= dist. Overlap of kmer not allowed'''

    sequence = formatFasta(sequence)

    count = 0
    i = 0
    while i < len(sequence):
        block = sequence[i : i + len(kmer)]
        if hammDist(block, kmer) >= dist:
            count += 1
            i += len(kmer)
        else :
            i += 1
    
    return count

fileI, kmer, dist = sys.argv[1], sys.argv[2], int(sys.argv[3])
print(neighbourCount(fileI, kmer, dist))