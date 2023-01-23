## Part TWO: PyPoll

#INITIAL SETUP: import modules that will be used for analysis
import csv #import module to use csv reader
import os #import module to leverage os to set relative path


#SETUP: Set relative path to the csv file containing the data I will analyze
csvpath = os.path.join("Resources", "election_data.csv") 

#SETUP: create lists that I will use to store data during analysis
allballots = [] #This essentially represents column 1 (month/yr)
c = []
vote_cand_1 = []
vote_cand_2 = []
vote_cand_3 = []


with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",") #this gets python to access and read the csv file

  csv_header = next(csvreader) #I am separating out the headers from the data set I'd like to analyze
  #print(csv_header) 
  
  for row in csvreader:
    allballots.append(row[0]) #Create list with values from column 1 (ballot ID)
    c.append(row[2]) #create list with values form column 3 (candidates)


#problem 1.
total_votes = (len(allballots)) #this will count the number of ballots listed in the csv file, which represents the # of votes cast

#problem 2. 
unique_candidates = set(c) #creating a set from list containing data in third column. A set only pulls unique values
unique_candidates_list = list(unique_candidates) #changing the set to a list

#problem 3. The percent of votes each candidate received

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",") #this gets python to access and read the csv file

  csv_header = next(csvreader)

  for row in csvreader: 
    if row[2] == "Charles Casper Stockham":
      vote_cand_1.append(row[0]) #Create a list containing all votes cast for candidate 1

    elif row[2] == "Diana DeGette":
      vote_cand_2.append(row[0]) #Create a list containing all votes cast for candidate 2

    elif row[2] == "Raymon Anthony Doane": 
      vote_cand_3.append(row[0]) #Create a list containing all votes cast for candidate 3

num_votes_cand_1 = int(len(vote_cand_1)) #creating variable for # of votes cast for cand 2

num_votes_cand_2 = int(len(vote_cand_2)) #creating variable for # of votes cast for cand 2

num_votes_cand_3 = int(len(vote_cand_3)) #creating variable for # of votes cast for cand 3

#Problem 3 Final Calc: Divide # of votes for each candidate by total # of votes cast to determine percentage of each candidtes # votes
#note- the round function will round a number to two decimals.
cand_1_percent_votes = round(int(num_votes_cand_1) / int(total_votes) *100, 3) #to three decimal places
cand_2_percent_votes = round(int(num_votes_cand_2) / int(total_votes) *100, 3) #to three decimal places
cand_3_percent_votes = round(int(num_votes_cand_3) / int(total_votes) *100, 3) #to three decimal places



vote_by_cand = [num_votes_cand_1, num_votes_cand_2, num_votes_cand_3] #create list containing votes by candidate
#cand_name = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]


most_votes = int(max(vote_by_cand))

dictionary = {
  "votecount": [num_votes_cand_1, num_votes_cand_2, num_votes_cand_3],
  "cands": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
}


dictionary_2 = {
  "Charles Casper Stockham" : [num_votes_cand_1],
  "Diana DeGette": [num_votes_cand_2],
  "Raymon Anthony Doane": [num_votes_cand_3]
}#creating a dictionary that matches votes to candidates so that I can print key/candidate with highest number of votes


random = max(dictionary_2, key=dictionary_2.get) #determining the candidate with the highest number of votes


#PRINTING ANSWERS TO CHALLENGE PYPOLL IN TERMINAL
print("")
print("-------------------------")
print("Claire: Analysis of Election Results:" )
print("-------------------------")
print("Total Votes: " + str(total_votes))
  #Total Votes: 369711
print("-------------------------")
print(str(dictionary["cands"][0]) + " : " + str(cand_1_percent_votes) + "%  ("+ str(num_votes_cand_1) + ")")
  #Charles Casper Stockham: 23.049% (85213)
print("-------------------------")
print(str(dictionary["cands"][1]) + " : " + str(cand_2_percent_votes) + "%  ("+ str(num_votes_cand_2) + ")")
#Diana DeGette: 73.812% (272892)
print("-------------------------")
print(str(dictionary["cands"][2]) + " : " + str(cand_3_percent_votes) + "%  ("+ str(num_votes_cand_3) + ")")
#Raymon Anthony Doane: 3.139% (11606)
print("-------------------------")
print("The winner is: " + str((random)) + " " + str((max(vote_by_cand))))
print("-------------------------")



#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

output_path = os.path.join("analysis", "results.txt") #set relative path to print out as text file

with open(output_path, 'w') as t: 
  print(" ", file = t)
  print("-------------------------", file = t)
  print("Claire: Analysis of Election Results:", file = t)
  print("-------------------------", file = t)
  print("Total Votes: " + str(total_votes), file = t)
  #Total Votes: 369711
  print("-------------------------", file = t)
  print(str(dictionary["cands"][0]) + " : " + str(cand_1_percent_votes) + "%  ("+ str(num_votes_cand_1) + ")", file = t)
  #Charles Casper Stockham: 23.049% (85213)
  print("-------------------------", file = t)
  print(str(dictionary["cands"][1]) + " : " + str(cand_2_percent_votes) + "%  ("+ str(num_votes_cand_2) + ")", file = t)
#Diana DeGette: 73.812% (272892)
  print("-------------------------", file = t)
  print(str(dictionary["cands"][2]) + " : " + str(cand_3_percent_votes) + "%  ("+ str(num_votes_cand_3) + ")", file = t)
#Raymon Anthony Doane: 3.139% (11606)
  print("-------------------------", file = t)
  print("The winner is: " + str((random)) + " " + str((max(vote_by_cand))), file = t)
  print("-------------------------", file = t)
  

