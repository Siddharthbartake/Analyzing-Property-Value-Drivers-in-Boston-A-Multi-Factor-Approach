import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Filter out blank years from 'Property Built' and 'Property Remodeled' columns
filtered_data = data[(data['Property Built'].notnull()) | (data['Property Remodeled'].notnull())]

# Get the minimum and maximum years where data exists
min_year = min(filtered_data[['Property Built', 'Property Remodeled']].min())
max_year = max(filtered_data[['Property Built', 'Property Remodeled']].max())

# Sort data by 'Total Property Value' in descending order and select top 50 rows
top_50_properties = filtered_data.nlargest(50, 'Total Property Value')

# Extract 'Property Built' and 'Property Remodeled' years for the top 50 properties
property_built_years = top_50_properties['Property Built']
property_remodeled_years = top_50_properties['Property Remodeled']
property_indices = range(1, len(top_50_properties) + 1)

# Plotting the values
plt.figure(figsize=(10, 6))
plt.plot(property_indices, property_built_years, label='Property Built', color='blue', marker='o')
plt.plot(property_indices, property_remodeled_years, label='Property Remodeled', color='green', marker='o')
plt.xlabel('Property Index (Top 50 Highest Total Property Value)')
plt.ylabel('Year')
plt.title('Property Built vs Property Remodeled for Top 50 Highest Total Property Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)  # Add grid lines for better readability

# Set y-axis limits based on the minimum and maximum years with data
plt.ylim(min_year, max_year)

# Annotate the graph with the least and latest property built years on the right side
plt.text(len(top_50_properties) + 1, min_year, f'Least Property Built Year: {min_year}', fontsize=10, ha='left', va='bottom')
plt.text(len(top_50_properties) + 1, max_year, f'Latest Property Built Year: {max_year}', fontsize=10, ha='left', va='top')

# Show plot
plt.tight_layout()
plt.show()
