# python-challenge
### PyBank
1. Created main.py in subfolder to analyze budget_data.csv for:
  + The total number of months included in the dataset
  + The net total amount of "Profit/Losses" over the entire period
  + The changes in "Profit/Losses" over the entire period, and then the average of those changes
  + The greatest increase in profits (date and amount) over the entire period
  + The greatest decrease in profits (date and amount) over the entire period
  + Print that analysis in terminal, and export a text file

### PyPoll
1. Created main.py in subfolder to analyze election_data.csv for:
  + Total number of votes cast
  + Complete list of candidates who received votes
    + Created a list of candidates, and printed it in terminal to see the list of unique candidates. Deleted this line of code as no longer necessary
    + Then assigned each entry in the list to a separate variable 
  + Percentage of votes each candidate won
    + Found total number of votes each candidate won first, and then stored each percentage as a variable to round them to 3 places
  + Total number of votes each candidate won
  + Winner based on popular vote
    + Created a list of the three vote totals, and used the max() function to find the highest entry.
    + Ran an if/elif/elif series to compare winning vote total to individual vote totals to assign winning candidate
  + Print that analysis in terminal, and export a text file
