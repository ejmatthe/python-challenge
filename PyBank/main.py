#Import module
import os
import csv

#Set path for CSV and set values of variables
csv_path = "Resources/budget_data.csv"
output_path = "output.txt"
net_change = 0
changes = []
greatest_inc = 1
greatest_dec = 0

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #Read and store header row
    csv_head = next(csv_reader)
    #Calculate total months
    total_months = (len(list(csv_reader)))

#Calculate net profit/loss
with open(csv_path) as csv_change:    
    csv_change_reader = csv.reader(csv_change, delimiter=",")
    next(csv_change_reader)
    for row in csv_change_reader:
        net_change += int(row[1])
        changes.append(int(row[1]))
        #Find greatest increase and decrease in profits (date and amount) over the entire period
        #If new greatest increase and new greatest decrease
        if int(row[1]) > greatest_inc:
            inc_month = str(row[0])
            greatest_inc = int(row[1])
        elif int(row[1]) < greatest_dec:
            dec_month = str(row[0])
            greatest_dec = int(row[1])
    
#Calculate average of changes in profit/loss
changes_sum = sum(changes)
changes_mean = round((changes_sum / total_months), 2)

#Print analysis to terminal
print("Financial Analysis")
print("")
print("----------------------------")
print("")
print(f"Total Months: ${total_months}")
print("")
print(f"Total: ${net_change}")
print("")
print(f"Average Change: ${changes_mean}")
print("")
print(f"Greatest Increase in Profits: {inc_month} ({greatest_inc})")
print("")
print(f"Greatest Decrease in Profits: {dec_month} ({greatest_dec})")

#Export as text file
with open(output_path, 'w') as outputfile:
    outputfile.write("Financial Analysis\n")
    outputfile.write("\n")
    outputfile.write("----------------------------\n")
    outputfile.write("\n")
    outputfile.write(f"Total Months: {total_months}\n")
    outputfile.write("\n")
    outputfile.write(f"Total: ${net_change} \n")
    outputfile.write("\n")
    outputfile.write(f"Average Change: ${changes_mean}\n")
    outputfile.write("\n")
    outputfile.write(f"Greatest Increase in Profits: {inc_month} ({greatest_inc})\n")
    outputfile.write("\n")
    outputfile.write(f"Greatest Decrease in Profits: {dec_month} ({greatest_dec})\n")