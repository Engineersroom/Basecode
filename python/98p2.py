# %%

import csv

filename = 'cwurData_4years.csv'
header = 'year'
filter_value = '2012'
A = []
B = []

# Filter the data based on the year
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row[header] == filter_value:
            A.append(row)

header = 'country'
filter_value = 'USA'

# Filter the data based on the country
for row in A:
    if row[header] != filter_value:
        B.append(row)

# Sort the data based on quality_of_education
sorted_data = sorted(B, key=lambda x: int(x['quality_of_education']))

selected_headers = ['quality_of_education', 'country', 'institution']
new_data = []

# Select the desired headers and create a new data list
for row in sorted_data:
    new_row = {header: row[header] for header in selected_headers}
    new_data.append(new_row)

filename = 'result.csv'

# Write the new data to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=selected_headers)
    writer.writeheader()
    writer.writerows(new_data)

print(f"Data has been successfully written to {filename}.")

# %%
