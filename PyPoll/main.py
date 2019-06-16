import os
import csv
import operator
import collections # Imported Pythong collections so I could use "Counter"

csvpath = os.path.join("election_data.csv")
csvfile = open(csvpath)
data = csvfile.read()

# VARIABLES
total_votes = 0
total_county = 0
votes = collections.Counter()   # Here is where I am associating "Counter" to the variable "votes". Counter will allow me to 
                                # identify a unique value and then add up all of the values associatd with the unique value.
                                # In this case, I am adding up all of the individual voterID's associated with each candicate.
                                # The results will be stored in a dictionary.  Key = Candidate name, Value = Number of Votes received 

# DICTIONARIES
results = {}                                    # Dictionary where results from counter will be stored

# LISTS
unique_candidate = []                           # I needed to create a list so I could move the dictionary resul

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)                # Need to skip first row (header row) so this row is not included in any counts

    for row in csvreader:
        votes[row[2]] += 1                      # The results from this line will give me the candidate and total votes they received
        total_votes = total_votes + 1           # Counting the lines of data in the entire csv file to get the Total Votes of 3,521,001  
    for key,value in sorted(votes.items()):
        results.update({key: "{:.2%}".format(value/total_votes)})   # Updating dictionary with candidate name and calculating/formatting 
                                                                    # percentage value of total votes received
    unique_candidate.append(results)                                # Appending dictionary values to a list

print("\n")
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes:,.0f}")
print("-----------------------------")
print("\n")
print(unique_candidate)
print("\n")

#end of the program

