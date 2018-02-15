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
with open('clean_orgs.csv') as dd_csv:
    # read the file into an object. https://docs.python.org/3/library/csv.html
    orgs = csv.reader(dd_csv, delimiter='|')
    # for each line
    for row in orgs:
        if len(row) != 3:
            continue
        orgs_list.append(Org(row[0],row[1],row[2]))

#print(str(orgs_list[0]))

relatedness = compare('levenshtein',0.8,0.95,orgs_list[2].name,orgs_list[4].name)
print("Relatedness: "+str(relatedness))
