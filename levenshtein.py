# pip3 install fuzzywuzzy --user
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys

# Input is two strings. Spaces must be replaced by underscores.
if len(sys.argv) < 3 or len(sys.argv) > 4 or len(sys.argv[-1]) < 3 or len(sys.argv[-2]) < 3:
    raise ValueError("Invalid input to levenshtein.")

print(fuzz.ratio(sys.argv[-1].replace("_"," "), sys.argv[-2].replace("_"," ")))

