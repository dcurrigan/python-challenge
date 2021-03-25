import os
import csv

dirname = os.path.dirname(__file__)
csv_path = os.path.join(dirname, 'Resources', 'budget_data.csv')

# Convert data to list and store headers separately 
with open(csv_path) as file:
    reader = csv.reader(file)
    data = []
    headers = next(reader)
    
    for line in csv.reader(file):
        data.append(line)

# Get number of months 
num_months = len(data)

# Get combined total for profit/loss
profit_loss_total = 0
for row in range(len(data)):
    profit_loss_total += int(data[row][1])

# Get change in profit/loss between months (current month total - previous month total)
change = []
greatest_increase = [0,0]
greatest_decrease = [0,0]

for row in range (1, len(data)):
    current_change = int(data[row][1]) - int(data[(row-1)][1])
    change.append(current_change)
    
    # check if greatest increase/decrease
    if current_change > greatest_increase[1]:
        greatest_increase[1] = current_change
        greatest_increase[0] = data[row][0]
    if current_change < greatest_decrease[1]:
        greatest_decrease[1] = current_change
        greatest_decrease[0] = data[row][0] 

# Get average change         
average_change = round((sum(change)/len(change)),2)

# print to terminal 
print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${profit_loss_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
print() 

# Write to txt file
output_file = os.path.join(dirname, "Analysis", "financial_analysis.txt")

with open(output_file, "w", newline="") as writer:
    nl = "\n"
    writer.write(f"Financial Analysis{nl}----------------------------{nl}") 
    writer.write(f"Total Months: {num_months}{nl}Total: ${profit_loss_total}{nl}") 
    writer.write(f"Average Change: ${average_change}{nl} 
    writer.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}){nl}") 
    writer.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}){nl}") 


