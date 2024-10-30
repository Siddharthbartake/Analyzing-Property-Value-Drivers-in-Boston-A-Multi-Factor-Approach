import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Filter data for specified Crime Neighborhoods
selected_neighborhoods = ['East Boston', 'South Boston', 'South End', 'Dorchester', 'Roxbury', 'Allston', 'Brighton', 'Charlestown', 'Fenway', 'Hyde Park', 'Jamaica Plain', 'Leather District', 'Mission Hill', 'West Roxbury']
filtered_data = data[data['Crime Neighborhood'].isin(selected_neighborhoods)]

# Plotting Total Property Value vs. Crime Incident Year for each Crime Neighborhood
plt.figure(figsize=(12, 8))

for neighborhood in selected_neighborhoods:
    neighborhood_data = filtered_data[filtered_data['Crime Neighborhood'] == neighborhood]
    sns.lineplot(data=neighborhood_data, x='Crime Incident Year', y='Total Property Value', label=neighborhood)

plt.title('Total Property Value Over Time for Selected Crime Neighborhoods')
plt.xlabel('Crime Incident Year')
plt.ylabel('Total Property Value')
plt.legend(title='Crime Neighborhood')
plt.tight_layout()
plt.show()
