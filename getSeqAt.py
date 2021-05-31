#FOR SHELL USE : python getSeqAt file start end 
#HELP : python getSeqAt.py -h

import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='Return a sequence from position start to position end (inclusive). Follows 0 indexing',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
parser.add_argument('start', type=int, default=0, help='START')
parser.add_argument('end', type=int, default=0, help='END')
args = parser.parse_args()


def getSeqAt(sequence, start, end):
    '''Return a sequence from position start to position end (inclusive). Follows 0 indexing.'''

    return formatFasta(sequence)[start : end + 1]

seq, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
print(getSequenceFrom(seq, start, end))