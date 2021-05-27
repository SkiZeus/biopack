#FOR SHELL USE : python kmerCount file "kmer"
#HELP : python kmerCount -h

import sys, argparse

#Help documentation
parser = argparse.ArgumentParser(
    description='Return the number of times a kmer appears in a fasta sequence. Kmers cannot overlap.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('f', type=str, default='', help='FILE')
parser.add_argument('k', type=str, default='', help='"KMER"')
args = parser.parse_args()

def formatFasta(fasta):
    '''Helper function which takes in a .fa file and returns the DNA sequence as a string, without any new line '\n'  or non nucleotide characters.'''

    fastaStr = ''
    with open(fasta, 'r') as fh:
            for line in fh.readlines()[1:]:
                fastaStr += line
    
    fastaStr = fastaStr.replace('\n', '').strip()
    return fastaStr
    
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