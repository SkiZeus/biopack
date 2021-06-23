#FOR SHELL USE : python3 kmerCount.py file "kmer"
#HELP : python3 kmerCount.py -h

import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='Return the number of times a kmer appears in a fasta sequence. Kmers cannot overlap.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
parser.add_argument('kmer', type=str, default='', help='"KMER"')
args = parser.parse_args()

def kmerCount(sequence, kmer):
    '''return the number of times a kmer appears in a given sequence. kmers cannot overlap.'''

    sequence = formatFasta(sequence)
    count = 0
    i = 0
    while i < len(sequence):
        if sequence[i : i + len(kmer)] == kmer:
            count += 1
            i += len(kmer)
        else :
            i += 1
    
    return count

seq, kmer = sys.argv[1], sys.argv[2]
print(kmerCount(seq, kmer))