import random

# Input is two strings and returns value from 0 to 100
def nlp(org1, org2):
    if len(org1) < 2 or len(org2) < 2:
        raise ValueError("Invalid input to nlp: |"+org1+"|"+org2+"|")
# do natural language processing stuff
    return random.randint(0,1)

