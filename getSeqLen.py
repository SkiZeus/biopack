#FOR SHELL USE : python getSeqLen file 
#HELP : python getSeqLen.py -h

import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='Return fasta sequence length - works for single entry fasta files.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
args = parser.parse_args()

def getSeqLen(sequence):
    '''Return fasta sequence length - works for single entry fasta files.'''

    return len(formatFasta(sequence))

seq = sys.argv[1]
print(getSeqLen(seq))