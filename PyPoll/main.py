import os
import csv

dirname = os.path.dirname(__file__)
csv_path = os.path.join(dirname, 'Resources', 'election_data.csv')

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
        # Lambda function returns the second element of the results list (votes), which is used as key to sort, in descenting order          
results.sort(key=lambda e:e[1], reverse=True)

# Print to terminal 
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for row in range (len(results)):
    print(f"{results[row][0]}: {results[row][2]}% ({results[row][1]})")
print("-------------------------")
print(f"Winner: {results[0][0]}")
print("-------------------------")
print()

# Write to txt file
output_file = os.path.join(dirname, "Analysis", "electoral_analysis.txt")

with open(output_file, "w", newline="") as writer:
    nl = "/n"
    writer.write(f"Election Results{nl}-------------------------{nl}"
    writer.write(f"Total Votes: {total_votes}{nl}-------------------------")
    for row in range (len(results)):
        writer.write(f"{results[row][0]}: {results[row][2]}% ({results[row][1]}){nl}") 
    writer.write(f"-------------------------{nl}Winner: {results[0][0]}{nl}-------------------------")


