# pip3 install fuzzy --user
import fuzzy

# Input is two strings0
def nysiis(org1, org2):
    if len(org1) < 3 or len(org2) < 3:
        raise ValueError("Invalid input to nysiis.")
    pronounciation1 = fuzzy.nysiis(org1)
    #print(org1+"|"+pronounciation1)
    pronounciation2 = fuzzy.nysiis(org2)
    #print(org2+"|"+pronounciation2)
    if pronounciation1 == pronounciation2:
        return 1
    else:
        return 0

