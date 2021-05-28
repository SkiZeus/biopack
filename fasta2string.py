import sys, argparse

#Help documentation
parser = argparse.ArgumentParser(
    description='Remove header from fasta file.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('f', type=str, default='', help='FILE')
args = parser.parse_args()

def formatFasta(fasta):
    '''Helper function which takes in a .fa file and removes header.'''

    fastaStr = ''
    with open(fasta, 'r') as fh:
            for line in fh.readlines()[1:]:
                fastaStr += line
    
    fastaStr = fastaStr.replace('\n', '').strip()
    return fastaStr
file, size = sys.argv[1]
print(formatFasta(file))