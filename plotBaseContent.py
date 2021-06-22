import matplotlib.pyplot as pyplot
from biopack import formatFasta

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
    pyplot.title(sequence + " Base Content Profile")
    pyplot.xlabel("DNA Base")
    pyplot.ylabel("% Distribution")
    pyplot.show()

print(baseContentPlot("seq.fa"))
#make bar plot
#add shell capability