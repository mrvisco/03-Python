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





    
