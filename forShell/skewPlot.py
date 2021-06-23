import matplotlib.pyplot as pyplot
import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='construct a skew plot: the difference between the total number of occurences of G and the total number of occurences of C in the first i nucletotides of a sequence.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
args = parser.parse_args()

def countSkew(sequence, index):
    '''Calculate skew value of a sequence up to position index'''

    skew = 0
    for i in sequence[:index]:
        if i == "G":
            skew += 1
        elif i == "C":
            skew -= 1
    
    return skew

def skewPlot(sequence): 
    '''construct a skew plot: the difference between the total number of occurences of G and the total number of occurences of C in the first i nucletotides of a sequence. Skew @ 0 = 0.'''
    sequence = formatFasta(sequence)

    xvals = [i for i in range(len(sequence))]
    yvals = [countSkew(sequence, i) for i in range(len(sequence))]

    #increasing, decreasing, neutral skew
    x1, x2, x3 = [], [], []
    y1, y2, y3 = [], [], [] 
    c1, c2, c3 = "g", "r", "black"

    for i in range(len(sequence)):
        if sequence[i] == "G":
            x1.append(i)
            y1.append(countSkew(sequence, i))
        elif sequence[i] == "C":
            x2.append(i)
            y2.append(countSkew(sequence, i))
        else:
            x3.append(i)
            y3.append(countSkew(sequence, i))

    #scatter coloured points
    
    pyplot.scatter(x1, y1, color= c1, s=30, label="increasing GC content")
    pyplot.scatter(x2, y2, color= c2, s=30, label="decreasing GC content")
    pyplot.scatter(x3, y3, color= c3, s=30, label="unchanging GC content")
    
    #pyplot.legend(bbox_to_anchor=(1, 1)) outside of graph
    pyplot.legend(loc='lower left')
    
    for i in range(len(sequence)):
        if i in x1:
            c = c1
        elif i in x2:
            c = c2
        elif i in x3:
            c = c3
        pyplot.plot([i, i + 1], [countSkew(sequence, i), countSkew(sequence, i + 1)], color = c, linewidth=3)

    pyplot.title("Genomic Skew Plot")
    pyplot.xlabel("Genome Position")
    pyplot.ylabel("Skew Count : (#G's - #C's)")
    pyplot.tight_layout()
    pyplot.show()

file = sys.argv[1]
print(skewPlot(file))