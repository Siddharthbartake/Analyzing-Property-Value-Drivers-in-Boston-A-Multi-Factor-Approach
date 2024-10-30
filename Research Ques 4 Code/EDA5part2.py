import pandas as pd

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Sort data by 'Total Property Value' in descending order and select top 50 rows
top_50_properties = data.nlargest(50, 'Total Property Value')

# Get distinct estate street numbers for the top 50 properties
distinct_estate_street_numbers = top_50_properties['Estate Street Number'].unique()

# Print the distinct estate street numbers
print("Distinct Estate Street Numbers for the Top 50 Properties:")
for street_number in distinct_estate_street_numbers:
    print(street_number)
