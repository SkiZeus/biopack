#FOR SHELL USE : python3 getTaxId.py inputFile OutputFile
#HELP : python3 getTaxId.py -h

import sys, argparse, csv, getopt
from Bio import Entrez
Entrez.email = "wlodarsm@mcmaster.ca"

''' PURPOSE:
from a .csv list of pathogens as such:
Achromobacter xylosoxidans
Acinetobacter baumannii
Acinetobacter defluvii

Write out new .csv with ncbi-genome-download approriate format:
Achromobacter_xylosoxidans,85698
Acinetobacter_baumannii,470
Acinetobacter_defluvii,1871111
'''

#Help documentation for shell
parser = argparse.ArgumentParser(
    description='Given a .csv file, with species name, write a new .csv with taxid appended to each name.',
    epilog='Written by Mateusz Wlodarski, https://github.com/Zeus-ski')
parser.add_argument('inputFile', type=str, help='choose inputFile .csv')
parser.add_argument('outputFile', type=str, help='choose outputFile .csv')
args = parser.parse_args()

def createSpeciesList(file):
    '''create python list with species names from .csv file'''

    with open(file, 'r') as fh:
        speciesList = [i[0] for i in csv.reader(fh)] #list with all species

    return speciesList

def get_taxid_from_species(fileI, fileO):
    '''write out new csv file with species,taxid format from list of just species'''
    
    speciesList = createSpeciesList(fileI)

    with open(fileO, 'w') as fh:
        for species in speciesList:
            search = Entrez.esearch(term=species, db="taxonomy", retmode="xml")
            record = Entrez.read(search)
            taxid = record['IdList'][0]
            species = species.replace(" ", "_")
            
            line = f'{species},{taxid}' #proper species_name,taxid format
            print(line, file=fh)
    
    print("check current directory for output file: " + fileO)

#Call from shell
fileI, fileO = sys.argv[1], sys.argv[2]

#Call from IDE 
#fileI, fileO = 'june_list_C.csv', 'pathy.csv'
print(get_taxid_from_species(fileI, fileO))
