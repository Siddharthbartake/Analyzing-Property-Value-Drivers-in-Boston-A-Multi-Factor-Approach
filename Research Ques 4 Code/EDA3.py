import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Filter out rows with missing values in 'Building Value' or 'Estate Address'
filtered_data = data.dropna(subset=['Building Value', 'Estate Address'])

# Sort the data by 'Building Value' in descending order and select the top 100 entries
top_100_building_values = filtered_data.sort_values(by='Building Value', ascending=False).head(100)

# Plotting the relationship between 'Building Value' and 'Total Property Value' for the top 100 estate addresses
plt.figure(figsize=(12, 8))
for estate_address in top_100_building_values['Estate Address'].unique():
    estate_data = top_100_building_values[top_100_building_values['Estate Address'] == estate_address]
    sns.scatterplot(data=estate_data, x='Building Value', y='Total Property Value', label=estate_address)

plt.title('Relationship B/w Building Value and Total Property Value for Top 100 Maximum Building Values with Estate Addresses')
plt.xlabel('Building Value')
plt.ylabel('Total Property Value')
plt.legend(title='Estate Address', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
