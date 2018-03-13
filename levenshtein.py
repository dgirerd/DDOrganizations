# pip3 install fuzzywuzzy --user
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys

# Input is two strings and returns value from 0 to 100
def levenshtein(org1, org2):
    if len(org1) < 2 or len(org2) < 2:
        raise ValueError("Invalid input to levenshtein: |"+org1+"|"+org2+"|")

    return fuzz.ratio(org1, org2)

#print(levenshtein("Pacific Heights Chevron","Chevron Corp."))
