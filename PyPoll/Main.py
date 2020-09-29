# Pull CSV

import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

cand_votes= {}
cand= []
percent_vote=[]
total_votes=0
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header= next(csvreader)

    for row in csvreader:
        cand=row[2]

        if cand in cand_votes.keys():
            cand_votes[cand]+=1
        else:
            cand_votes[cand]=1

total_votes= sum(cand_votes.values())
print(total_votes)
for i in cand_votes:
    percent_vote= round((float(cand_votes[i])/total_votes)*100,2)

    print(f"{i} {percent_vote} {cand_votes[i]}")

for key in cand_votes.keys():
    if cand_votes[key]==max(cand_votes.values()):
        winner=key

print("Winner:"+winner)    

