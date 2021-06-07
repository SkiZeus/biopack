def hammDist(seqA, seqB):
    '''Returns the Hamming distance between two sequences of equal length'''

    mismatch = 0
    try:
        for i in range(len(seqA)):
            if seqA[i] != seqB[i]:
                mismatch += 1
    except:
        print("Error: equal sequence lengths are required to compute Hamming distance.")
    
    return mismatch

print(hammDist("atg", "at"))