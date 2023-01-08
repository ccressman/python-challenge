#PART ONE: PyBank

#INITIAL SETUP: Setting up python to read the csv file so that I can then analyze the data
import csv #import module to use csv reader
import os #import module to leverage os to set relative path

#INITIAL SETUP: #setting the relative path to the csv I need to analyze
csvpath = os.path.join("Resources", "budget_data.csv")

#INITIAL SETUP: create lists that I will use to store data for calculations/manipulation
allmonths = [] #This essentially represents column 1 (month/yr)
p_l = [] #This list will contain column 2 values (profit and loss column)

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",") #this gets python to access and read the csv file

  csv_header = next(csvreader) #I am separating out the headers from the data set I'd like to analyze
  
  for row in csvreader:
    allmonths.append(row[0]) #I am making a list with values from column 1

    p_l.append((int(row[1]))) #I am making a list with values from column 2. It contains a mix of int and string (error when I used sum function initially) so I am casting to integer as a I move the data points to the list

plsum = sum(p_l)

changement = [vi - vii for vii, vi in zip(p_l[: -1], p_l[1 :])] #using zip file to offset the list of profit and loss by one and subtract the difference
l = len(changement) #calculates the number of values
s = sum(changement) #calculates the total value of the numbers
mn = round(s / l, 2) #calculates the average by dividing the sum of values by the number of values in the dataset


month_set = set(allmonths) #making a set of the allmonths list to make sure no months are repeated (doesn't look to be the case, but did it anyway. I think the unique function is only used with pandas)


#THE MOMENT OF TRUTH!! GOING TO PRINT OUT THE REQUESTED RESULTS BELOW!
print("----------------------------")
print("Claire: Financial Analysis")
print("----------------------------")
  #Total Months: 86
print("Total Months Included in Dataset: " + str(len(month_set)) + " months")
print("")
  #Total: $22564198
print("Net Total of Profit and Loss: $" + str(plsum))  #use sum function to sum profit and loss values. This calculates the total net change
print("")
  #Average Change: $-8311.11
print("Average Change in Profit and Loss Between Months Reported: $" + str((mn)))
print("")

print("Greatest Increase in Profit and Loss: $" + str(max(changement)))
print("")

print("Greatest Decrease in Profit and Loss: $" + str(min(changement)))
print("")

print("The End! Hope the negative numbers weren't too depressing.")


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_path = os.path.join("analysis", "results.txt") #set relative path to print to text file

with open(output_path, 'w') as t: 
  print("----------------------------", file = t)
  print("Claire: Financial Analysis", file = t)
  print("----------------------------", file = t)
  print("Total Months Included in Dataset: " + str(len(month_set)) + " months", file = t)
  print("", file = t)
  print("Net Total of Profit and Loss: $" + str(plsum), file = t)  
  print("", file = t)
  print("Average Change in Profit and Loss Between Months Reported: $" + str((mn)), file = t)
  print("", file = t)
  print("Greatest Increase in Profit and Loss: $" + str(max(changement)), file = t)
  print("", file = t)
  print("Greatest Decrease in Profit and Loss: $" + str(min(changement)), file = t)
  print("", file = t)
  print("The End! Hope the negative numbers weren't too depressing.", file = t)
  
  