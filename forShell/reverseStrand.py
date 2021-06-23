#FOR SHELL USE : python reverseStrand file 
#HELP : python reverseStrand -h

import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='Return the reverse complement of a nucleotide fasta file.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('f', type=str, default='', help='FILE')
args = parser.parse_args()

def reverseStrand(sequence):
    '''Returns the reverse complement of a nucleotide fasta file.'''

    sequence = formatFasta(sequence)
    complement = ''
    for i in sequence:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'C':
            complement += 'G'
        elif i == 'G':
            complement += 'C'
    
    return complement[::-1] #reverse direction

seq = sys.argv[1]
print(reverseStrand(seq))


