#FOR SHELL USE : python countMismatches.py seqA seqB
#HELP : python countMismatches.py -h

import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='Returns the number of mismatches between two sequences of equal length.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
parser.add_argument('file', type=str, default='', help='FILE')
args = parser.parse_args()

def countMismatches(seqA, seqB):
    '''Returns the number of mismatches between two sequences of equal length'''

    seqA, seqB = formatFasta(seqA), formatFasta(seqB)

    mismatch = 0
    if len(seqA) != len(seqB):
        return "Error: equal sequence lengths are required to compute number of mismatches."
    else:
        for i in range(len(seqA)):
            if seqA[i] != seqB[i]:
                mismatch += 1
        return mismatch

file1, file2 = sys.argv[1], sys.argv[2]
print(countMismatches(file1, file2))