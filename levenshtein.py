# pip3 install fuzzywuzzy --user
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys

# Input is two strings and returns value from 0 to 100
def levenshtein(org1, org2):
    if len(org1) < 3 or len(org2) < 3:
        raise ValueError("Invalid input to levenshtein.")

    return fuzz.ratio(org1, org2)

