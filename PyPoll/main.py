#Import module
import os
import csv

#Set path for CSV and set values of variables
csv_path = "Resources/election_data.csv"
output_path = "output.txt"
votes_one = 0
votes_two = 0
votes_three = 0
cand_one = 'Charles Casper Stockham'
cand_two = 'Diana DeGette'
cand_three = 'Raymon Anthony Doane'
votes_list = []
cand_list = []



#Find total number of votes
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #Read and store header row
    csv_head = next(csv_reader)
    #Calculate total number of votes
    total_votes = (len(list(csv_reader)))

#Find candidates
with open(csv_path) as csv_change:    
    csv_vote_reader = csv.reader(csv_change, delimiter=",")
    next(csv_vote_reader)
    for row in csv_vote_reader:
        if row[2] not in cand_list:
            cand_list.append(row[2])
    cand_one = cand_list[0]
    cand_two = cand_list[1]
    cand_three = cand_list[2]
    
    
#Find vote totals    
with open(csv_path) as csv_count:
    csv_vote_counter = csv.reader(csv_count, delimiter=",")
    next(csv_vote_counter)
    for row in csv_vote_counter:
        if str(row[2]) == cand_one:
            votes_one = votes_one + 1
        elif str(row[2]) == cand_two:
            votes_two = votes_two + 1
        elif str(row[2]) == cand_three:
            votes_three = votes_three + 1


#Find vote percentages
    percent_one = round((votes_one / total_votes) * 100, 3)
    percent_two = round((votes_two / total_votes) * 100, 3)
    percent_three = round((votes_three / total_votes) * 100, 3)

#Find winner
votes_list.append(votes_one)
votes_list.append(votes_two)
votes_list.append(votes_three)
votes_winner = max(votes_list)
if votes_winner == votes_one:
    cand_winner = cand_one
elif votes_winner == votes_two:
    cand_winner = cand_two
elif votes_winner == votes_three:
    cand_winner = cand_three

#Print analysis to terminal
print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("-------------------------")
print("")
print(f"{cand_one}: {percent_one}% ({votes_one})")
print("")
print(f"{cand_two}: {percent_two}% ({votes_two})")
print("")
print(f"{cand_three}: {percent_three}% ({votes_three})")
print("")
print("-------------------------")
print("")
print(f"Winner: {cand_winner}")
print("")
print("-------------------------")

with open(output_path, 'w') as outputfile:
    outputfile.write("Election Results\n")
    outputfile.write("\n")
    outputfile.write("-------------------------\n")
    outputfile.write("\n")
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("\n")
    outputfile.write("-------------------------\n")
    outputfile.write("\n")
    outputfile.write(f"{cand_one}: {percent_one}% ({votes_one})\n")
    outputfile.write("\n")
    outputfile.write(f"{cand_two}: {percent_two}% ({votes_two})\n")
    outputfile.write("\n")
    outputfile.write(f"{cand_three}: {percent_three}% ({votes_three})\n")
    outputfile.write("\n")
    outputfile.write("-------------------------\n")
    outputfile.write("\n")
    outputfile.write(f"Winner: {cand_winner}\n")
    outputfile.write("\n")
    outputfile.write("-------------------------\n")