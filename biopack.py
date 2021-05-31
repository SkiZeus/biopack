'''Biopack by Mateusz Wlodarski, https://github.com/Zeus-ski

Frequently invoked methods needed for other biopack python scripts for shell use, ensure biopack.py is in the same directory as other biopack scripts. 

formatFasta is the engine that turns single entry fasta files into strings.'''

#Modules
def formatFasta(fasta):
    '''Remove fasta header and return sequence as a string. Works for single entry fasta files.'''

    fastaStr = ''
    with open(fasta, 'r') as fh:
            for line in fh.readlines()[1:]:
                fastaStr += line
    
    fastaStr = fastaStr.replace('\n', '').strip()
    
    return fastaStr

def kmerCount(sequence, kmer):
    '''Return the number of times a kmer appears in a given sequence. kmers cannot overlap: ex: "ATATA", "ATA" -> returns 1.'''

    count = 0
    i = 0
    while i < len(sequence):
        if sequence[i : i + len(kmer)] == kmer:
            count += 1
            i += len(kmer)
        else :
            i += 1
    
    return count

def getSeqAt(sequence, start, end):
    '''Return a sequence from position start to position end (inclusive). Follows 0 indexing.'''

    return sequence[start : end + 1]

def reverseStrand(sequence):
    '''Returns the reverse complement of a nucleotide sequence.'''

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
    
    return complement[::-1] 

def getSeqLen(sequence):
    '''Return sequence length.'''

    return len(sequence)