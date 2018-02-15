import csv

# open csv file
with open('orgs_orgconcepts.csv') as dd_csv:
        # read the file into an object. https://docs.python.org/3/library/csv.html
        orgs = csv.reader(dd_csv, delimiter=',')
        to_write = ["org_id,org_name,concept_id"]
        # for each line
        for row in orgs:
            # ignore lines missing values
            if len(row) == 5:
                # Check input values
                if row[2][1:].isdigit():
                    # If valid input make string of org_name,concept_id and add to list
                    to_write.append(str(row[0]+"|"+row[1]+"|"+row[2][1:]))
    #    print(to_write)
        # write to file
        with open("clean_orgs.csv",'w') as clean:
            clean.write('\n'.join(to_write))
