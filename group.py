# takes in a csv of orgs, calls compare with a certain method and evaluates accuracy

import csv
from compare import compare

class Org:


    def __init__(self, oid, name, cid):
        self.oid = oid
        self.name = name
        self.cid = cid

    def __str__(self):
        return self.oid+' | '+self.name+' | '+self.cid

orgs_list = []
# open csv file
with open('orgs_test_set.csv') as dd_csv:
    # read the file into an object. https://docs.python.org/3/library/csv.html
    orgs = csv.reader(dd_csv, delimiter=',')
    # for each line
    for row in orgs:
        if len(row) != 3:
            continue
        orgs_list.append(Org(row[0],row[1],row[2]))

#print(str(orgs_list[0]))
counter = 0
correct = 0
matched = 0
not_matched = 0
orgs_list2 = list(orgs_list)
for org1 in orgs_list:
    for org2 in orgs_list2:
        if org1.oid == org2.oid:
            continue
        counter += 1
        relatedness = compare('levenshtein', 0.8, 0.95, org1.name, org2.name)
        if org1.cid == org2.cid:
            if relatedness > 0:
                correct += 1
                matched +=1
            else:
                not_matched += 1
        if (relatedness == 0 and org1.cid != org2.cid):
            correct += 1
        
print("Count: "+str(counter)+" Correct: "+str(correct)+" Percentage: "+str(correct/counter))
print("Related: "+str(matched+not_matched)+" Correct: "+str(matched)+" Percentage: "+str(matched/(matched+not_matched)))
