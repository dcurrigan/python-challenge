import os
import csv

dirname = os.path.dirname(__file__)
csv_path = os.path.join(dirname,'Resources', 'employee_data.csv')

# Convert open data file to list and store headers
with open(csv_path) as file:
    reader = csv.reader(file)
    data = []
    headers = next(reader)
    
    for line in csv.reader(file):
        data.append(line)

# Dictionary of state abbreviations
us_state_abbrev = { 'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
                    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
                    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
                    }

# Split name into first and surname. Additional Headers added to header object
headers.insert(2,"Surname")
headers[1] = "First name"
for row in range(len(data)):
    fullname = data[row][1].split(" ")
    data[row].insert(2, fullname[1])
    data[row][1] = fullname[0]

# Change date formatting
for row in range(len(data)):
    split_date = data[row][3].split("-")
    data[row][3] = split_date[1] + "-" + split_date[2] + "-" + split_date[0]

# Change SSN formatting
for row in range(len(data)):
    split_ssn = data[row][4].split("-")
    data[row][4] = "***" + "-" + "**" + "-" + split_ssn[2]

# Change state formatting to 2-letter abbrevations using dictionary
for row in range(len(data)):
    data[row][5] = us_state_abbrev[data[row][5]]

output_path = os.path.join(dirname, "Output", "new_employee_data.csv")

# Print to CSV file
with open(output_path, 'w', newline="") as csvfile:

    csv_writer = csv.writer(csvfile, delimiter=',')

    # Write the header
    csv_writer.writerow(headers)

    # Write data
    for row in range(len(data)):
        csv_writer.writerow(data[row])