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
for row in range(0, len(data)):
    profit_loss_total += int(data[row][1])

# Get change in profit/loss 
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

average_change = round((sum(change)/len(change)),2)

# print to terminal 
print()
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(num_months))
print("Total: $"+ str(profit_loss_total))
print("Average Change: $"+ str(average_change))
print("Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")")
print() 


# Write to txt file
output_file = os.path.join(dirname, "Analysis", "financial_analysis.txt")

with open(output_file, "w", newline="") as writer:
    writer.write("Financial Analysis" + "\n" + "----------------------------" + "\n" + 
                 "Total Months: " + str(num_months) + "\n" + "Total: $"+ str(profit_loss_total) + "\n" + 
                 "Average Change: $"+ str(average_change) + "\n" + 
                 "Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")" + "\n" + 
                 "Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")") 


