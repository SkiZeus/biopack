import matplotlib.pyplot as pyplot
import sys, argparse
from biopack import formatFasta

#Help documentation
parser = argparse.ArgumentParser(
    description='Create basic bar plot that visualizes base content distribution of given sequence.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('file', type=str, default='', help='FILE')
args = parser.parse_args()

def baseContentPlot(sequence):
    '''Create basic bar plot that visualizes base content distribution of given sequence.'''
    seq = formatFasta(sequence)

    content = {"A": 0, "T": 0, "C": 0, "G": 0}

    for i in seq:
        content[i] += 1
    #print(list(content.values()))

    xvalues = list(content.keys())
    yvalues = [ i / len(seq) for i in list(content.values())]
    
    pyplot.bar(xvalues, yvalues, color=['red', 'blue', 'yellow', 'green'])
    pyplot.title(" Base Content Profile")
    pyplot.xlabel("DNA Base")
    pyplot.ylabel("% Distribution")
    pyplot.show()

file = sys.argv[1]
print(baseContentPlot(file))