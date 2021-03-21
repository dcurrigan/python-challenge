import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

# convert data to list 
with open(csv_path) as file:
    reader = csv.reader(file)
    data = []
    next(reader)
    
    for line in csv.reader(file):
        data.append(line)

# get number of months 
num_months = len(data)

# get combined total for profit/loss
profit_loss_total = 0
for row in range(0, len(data)):
    profit_loss_total += int(data[row][1])
print(profit_loss_total)

# get average change in profit/loss 
