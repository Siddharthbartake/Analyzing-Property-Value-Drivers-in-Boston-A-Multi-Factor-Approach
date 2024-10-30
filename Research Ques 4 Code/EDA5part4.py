import pandas as pd

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Sort data by 'Total Property Value' in ascending order and select the least 50 rows
least_50_properties = data.nsmallest(50, 'Total Property Value')

# Get distinct estate street numbers for the least 50 properties
distinct_estate_street_numbers = least_50_properties['Estate Street Number'].unique()

# Print the distinct estate street numbers
print("Distinct Estate Street Numbers for the Least 50 Lowest-Priced Properties:")
for street_number in distinct_estate_street_numbers:
    print(street_number)
