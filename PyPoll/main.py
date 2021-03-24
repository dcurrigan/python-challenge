import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

# Convert data to list and store headers
with open(csv_path) as file:
    reader = csv.reader(file)
    data = []
    headers = next(reader)
    
    for line in csv.reader(file):
        data.append(line)

# Get total votes (length of data set)
total_votes = len(data)

# Get list containing all candidate names (this represents the votes) 
votes = []
for row in range (0, len(data)): 
    votes.append(data[row][2])

# Get unique candidates
candidates = set(votes)

# Count votes for each candidate and sort by vote count in descending order
results = []
for person in candidates:
    # List with name, votes and percentage at each index
    results.append([person, votes.count(person), round((votes.count(person)/total_votes*100),3)])
        # Lambda function returns the second element of the results list (votes), which is used as key to sort           
results.sort(key=lambda e:e[1], reverse=True)

# Print to terminal 
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: " + str(total_votes))
print("-------------------------")
for row in range (0, len(results)):
    print(results[row][0] + ": " + str(results[row][2]) + "% (" + str(results[row][1]) + ")")
print("-------------------------")
print("Winner: " + results[0][0])
print("-------------------------")
print()

# Write to txt file
output_file = os.path.join("Analysis", "electoral_analysis.txt")

with open(output_file, "w", newline="") as writer:
    writer.write("Election Results" + "\n" + "-------------------------" + "\n" + 
                 "Total Votes: " + str(total_votes) + "\n" + "-------------------------" + "\n" ) 

    for row in range (0, len(results)):
        writer.write(results[row][0] + ": " + str(results[row][2]) + "% (" + str(results[row][1]) + ")" + "\n") 
    
    writer.write("-------------------------" + "\n" + "Winner: " + results[0][0] + "\n" + "-------------------------")


