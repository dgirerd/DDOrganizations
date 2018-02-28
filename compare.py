#python3 compare.py levenshtein 0.8 0.95 org1 org2


import sys
from levenshtein import levenshtein
from soundex import soundex
from nysiis import nysiis
# TODO import other methods



# @param method string which indicates which method to use
# @param related_threshold_str float between 0 and 1 setting minimum value for related
# @param same_threshold_str float between 0 and 1, setting minimum value for same, must be higher than related threshold
# @param org1 string of organization name with underscores replaced spaces
# @param org2 string of organization name with underscores replaced spaces
# return int 0, 1, or 2 representing relatedness
def compare(method, related_threshold_str, same_threshold_str, org1, org2):

    # Convert thresholds to floats
    related_threshold = float(related_threshold_str)
    same_threshold = float(same_threshold_str)

    # Check input parameters
    #if len(sys.argv) < 6:
    #    print("Missing arguments. Should have method, related_threshold, same_threshold, org1, org2")
    if related_threshold < 0 or related_threshold > 1:
        print("Invalid argument. Related threshold must be between 0 and 1 inclusive.")
        sys.exit()
    if same_threshold < 0 or same_threshold > 1:
        print("Invalid argument. Same threshold must be between 0 and 1 inclusive.")
        sys.exit()
    if related_threshold > same_threshold:
        print("Invalid argument. Related threshold must be less than same threshold.")
        sys.exit()
    if len(org1) > 200 or len(org2) > 200:
        print("Sanity check. Does this org really have a name over 200 characters?")
        sys.exit()

    if method.lower() == "levenshtein":
        levenshtein_score = levenshtein(org1, org2)
 #       print("Levenshtein score: "+str(levenshtein_score))
        normalized_score = levenshtein_score * 0.01
        if normalized_score > same_threshold:
            return 2
        elif normalized_score > related_threshold:
            return 1
        else:
            return 0

    if method.lower() == "soundex":
        return soundex(org1, org2)

    if method.lower() == "nysiis":
        return nysiis(org1, org2)
    #TODO other methods
    
    
    print("Invalid argument. Method not found.")
    sys.exit()


#relatedness = compare(sys.argv[-5], sys.argv[-4], sys.argv[-3], sys.argv[-2], sys.argv[-1])
#print("Relatedness: "+str(relatedness))
