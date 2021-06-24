'''Biopack by Mateusz Wlodarski, https://github.com/Zeus-ski

Frequently invoked methods needed for other biopack python scripts for shell use, ensure biopack.py is in the same directory as other biopack scripts. 

formatFasta is the engine that turns single entry fasta files into strings.'''

import os.path
#Modules
def formatFasta(fasta):
    '''Remove fasta header and return sequence as a string. Works for single entry fasta files.'''

    if os.path.isfile(fasta):
        fastaStr = ''
        with open(fasta, 'r') as fh:
                for line in fh.readlines()[1:]:
                    fastaStr += line
        
        fastaStr = fastaStr.replace('\n', '').strip()
    else :
        fastaStr = fasta
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

def hammDist(seqA, seqB):
    '''Returns the Hamming distance between two sequences of equal length'''

    mismatch = 0
    if len(seqA) != len(seqB):
        return "Error: equal sequence lengths are required to compute Hamming distance."
    else:
        for i in range(len(seqA)):
            if seqA[i] != seqB[i]:
                mismatch += 1
        return len(seqA) - mismatch
    
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