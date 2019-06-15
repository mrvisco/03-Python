import os
import csv
import operator
import collections

csvpath = os.path.join("election_data.csv")
csvfile = open(csvpath)
data = csvfile.read()

# variables
total_votes = 0
total_county = 0
name = None
ID = None
results = {}


#Lists
unique_candidate = []

votes = collections.Counter()
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # Need to skip first row (header row) so this row is not included in any counts

    for row in csvreader:
        votes[row[2]] += 1
        total_votes = total_votes + 1     # Counting the lines of data in the csv file   
    for key,value in sorted(votes.items()):
        print(key, value/total_votes)

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes:,.0f}")
print("-----------------------------")

print(votes)
print(len(votes))





'''
    print(csv_header)

    data_sort = sorted(csvreader,key=operator.itemgetter(2))
    #for eachline in sort:
        #print(eachline)

    for row in data_sort:
        if row[2] not in unique_candidate:
                unique_candidate.append(row[2])
        total_votes = total_votes + 1     # Counting the lines of data in the csv file
    print(unique_candidate)
    print(total_county)
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes:,.0f}")
    print("-----------------------------")
'''

    


    
