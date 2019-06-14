'''
Import os -- Imports OS Module functions allowing you to interface with underlying operating system
Python is running. 
Import csv -- Imports and provides access to the data file.
'''
import os
import csv
import operator

'''
csvpath is the path where the file is located
csvfile is reference name of the file
'''
csvpath = os.path.join("budget_data.csv")
csvfile = open(csvpath)

# csvfile.read() reads the records in the csv file and "stores" the records in "data"
data = csvfile.read()

# This section is where I created all of my variables and lists.  The variables allowed me to capture
# an end result or hold a value for future use.  The lists allowed me to segregate like/kind data
# for further analysis or to extract additional pieces of individual data (i.e. Min and Max values).

# variables
pandl = 0
mmyyyy = 0
preval = 0
curdiff = 0
average = 0
sumavg = 0
myavg = 0
plmax = 0
plmin = 0

# Lists
date = []         # Separate list of all dates in the CSV file
profitloss = []   # Separate list of all profit and loss values in CSV file
difference = []   # Unique list which will hold the calculation of the current profit & loss amount from the previous amount
ascending = []    # Sorted list so I could pick the minimum and maximum values

# This section is where I applied all of my logic or calculations.
# First step was to open the file I would be using for this section. 
with open(csvpath,newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader) # Need to skipt first row (header row) so this row is not included in any counts
   
   for row in csvreader:
      mmyyyy = mmyyyy + 1     # Counting the lines of data in the csv file
      pandl += float(row[1])  # Adding Profit and Loss numbers to get an aggregate 

      # Creating lists for use when creating a new 
      # csv file
      date.append(row[0])
      '''
      profitloss.append(row[1])  
      '''

      curdiff = float(row[1]) - preval # These three lines of code calculate monthly difference in profits         
      difference.append(curdiff)
      preval = float(row[1])
            
   date = date[1:]               # using [1:] skips over the row[0] or "date" that has a blank value
   difference = difference[1:]   # Starts the date and difference from appropriate line by skipping
   
   for row in difference:     # These four lines of code total the difference and then get average
      myavg = myavg + 1       
      sumavg += float(row)
   average = (sumavg/myavg)
   
   print("Financial Analysis")         # This section prints the Heading, dashed line and first three
   print("----------------------------") # answers of problem
   print(f"Total Months: {mmyyyy}")        
   print(f"Total: ${pandl:,.0f}") 
   print(f"Average Change: ${average:,.2f}")

# This section is creating a second csv file which I used to sort the differences so I could get the greatest
# increase and decrease along with the corresponding date
cleaned_csv = zip(date,difference) 
pair_list = sorted(cleaned_csv, key=operator.itemgetter(1),reverse=True)
#print(pair_list)

for row in pair_list:
   plmax = pair_list[0]
   plmin = pair_list[-1]
print(f"Greatest Decrease in Profits: {plmin}")
print(f"Greatest Increase in Profits: {plmax}")


# End of main.py