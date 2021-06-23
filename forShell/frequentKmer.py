#FOR SHELL USE : python frequentKmer file size
#HELP : python frequentKmer -h

import sys, argparse
from biopack import formatFasta, kmerCount

'''#Help documentation
parser = argparse.ArgumentParser(
    description='Given a fasta file, return the most frequent kmer(s) of length s.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
parser.add_argument('kmerSize', type=int, default=0, help='"SIZE"')
args = parser.parse_args()'''

def frequentKmer(sequence, size):
    '''Given a fasta sequence, return the most frequent kmer of length size.'''

    sequence = formatFasta(sequence)
    kmers = {}
    
    for i in range(len(sequence) - size):
        kmer = sequence[i : i + size]
        if kmer in kmers:
            kmers[kmer] += 1
        else :
            kmers[kmer] = 0
    
    best = max(kmers.values())
    result = ''

    for kmer in kmers.keys():
        if kmers[kmer] == best:
            result += kmer
            result += '\n'
    result.strip()

    result = f'most frequent kmer(s): \n{result}appear(s) {best} times'
    
    return result

file, size = sys.argv[1], int(sys.argv[2])
print(frequentKmer(file, size))