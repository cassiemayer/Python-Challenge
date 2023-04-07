import os
import csv

input_file = ('python-challenge', 'PyPoll', 'election_data.csv')

total_votes_casted = []
candidates_who_ran = { "CandidateOne" : "Charles Casper Stockham",
                      "CandidateTwo" : "Dianna Deggette",
                      "CandidateThree" : "Raymon Anthony Doane"}
candidate_who_won = {"Dianna Deggette" : "Winner"}

csvpath = './Resources/election_data.csv'

with open(csvpath, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        header = next(csvreader)
        for row in csvreader: 
                total_votes_casted.append(int(row[0]))
for candidates in candidates_who_ran:
        total_votes = len(total_votes_casted)



print("Election Results")
print("---")
print(f"total_votes: {total_votes}")
print(f"values({candidates_who_ran})")
print(candidate_who_won)

output_file = "./Analysis/election_data.txt"

with open(output_file,"w") as file:
        file.write("Election Results")
        file.write("\n")
        file.write("---")
        file.write("\n")
        file.write(f"Total Votes: {total_votes}")
        file.write("\n")
        file.write(f"{candidates}")
        file.write(f'{candidate_who_won}')