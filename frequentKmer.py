#FOR SHELL USE : python frequentKmer file size
#HELP : python frequentKmer -h

import sys, argparse

#Help documentation
parser = argparse.ArgumentParser(
    description='Given a fasta file, return the most frequent kmer(s) of length s.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('f', type=str, default='', help='FILE')
parser.add_argument('size', type=int, default=0, help='"SIZE"')
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

    count = 0
    i = 0
    while i < len(sequence):
        if sequence[i : i + len(kmer)] == kmer:
            count += 1
            i += len(kmer)
        else :
            i += 1
    
    return count

def frequentKmer(sequence, size):
    '''Given a fasta sequence, return the most frequent kmer of length size.'''

    sequence = formatFasta(sequence)
    kmers = [sequence[n : n + size] for n in range(len(sequence) - size + 1)]
    kmers = list(set(kmers))
    
    frequency = []
    for i in kmers:
        frequency.append((i, kmerCount(sequence, i)))
   
   
    best = max([frequency[i][1] for i in range(len(frequency))])
    result = ''
    for i in frequency:
        if i[1] == best:
            result += f'{i[0]} \n'

    result = f'most frequent kmer(s): \n{result}appear(s) {best} times'
    
    return result

file, size = sys.argv[1], int(sys.argv[2])
print(frequentKmer(file, size))