#FOR SHELL USE : python reverseStrand file 
#HELP : python reverseStrand -h

import sys, argparse

#Help documentation
parser = argparse.ArgumentParser(
    description='Return the reverse complement of a nucleotide fasta file.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('f', type=str, default='', help='FILE')
args = parser.parse_args()

def formatFasta(fasta):
    '''Remove fasta header.'''

    fastaStr = ''
    with open(fasta, 'r') as fh:
            for line in fh.readlines()[1:]:
                fastaStr += line
    
    fastaStr = fastaStr.replace('\n', '').strip()
    return fastaStr

def reverseStrand(sequence):
    '''Returns the reverse complement of a nucleotide fasta file.'''

    sequence = formatFasta(sequence)
    i = 0
    complement = ''
    while i < len(sequence):
        if sequence[i] == 'A':
            complement += 'T'
        elif sequence[i] == 'T':
            complement += 'A'
        elif sequence[i] == 'C':
            complement += 'G'
        elif sequence[i] == 'G':
            complement += 'C'
        i += 1
    
    return complement[::-1] #reverse direction
seq = sys.argv[1]
print(reverseStrand(seq))


