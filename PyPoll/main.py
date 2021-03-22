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

# Get total votes 
total_votes = len(data)

# Get candidates list
votes = []
for row in range (0, len(data)): 
    votes.append(data[row][2])

# Get unique candidates
candidates = set(votes)
print(candidates)

# Count votes for each candidates
# Creates a dictionary that hold the number and percentage of total votes for each candidate 
results = {}
for person in candidates:
    results[person] = {votes.count(person), round((votes.count(person)/total_votes*100),2)}

print(results)