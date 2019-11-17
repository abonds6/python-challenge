import os
import csv

# Create variables for calculations
candidates = []
number_votes = 0
vote_counts = []

# List of files 
election_data = ['1', '2']

# Loop through files
for files in election_data:
    # Get CSV
    from os.path import expanduser
    home = expanduser("~")
    election_data = os.path.join(home,"Downloads","PyPoll_election_data.csv")
    

    # Open current CSV
    with open(election_data) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        row = next(csvReader,None)

        # Calculate the votes
        for row in csvReader:
            number_votes = number_votes + 1
            candidate = row[2]

            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            else:
                candidates.append(candidate)
                vote_counts.append(1)

    # Setting the vote counts and percentages
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/number_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    percentages = [round(i,2) for i in percentages]

    # Print results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {number_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

