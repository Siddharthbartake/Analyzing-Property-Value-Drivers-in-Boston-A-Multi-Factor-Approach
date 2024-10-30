import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Sort data by 'Total Property Value' in ascending order and select the least 50 rows
least_50_properties = data.nsmallest(50, 'Total Property Value')

# Extract 'Property Built' and 'Property Remodeled' years for the least 50 properties
property_built_years = least_50_properties['Property Built']
property_remodeled_years = least_50_properties['Property Remodeled']

# Plotting the values
plt.figure(figsize=(10, 6))
plt.plot(property_built_years, label='Property Built', color='blue', marker='o')
plt.plot(property_remodeled_years, label='Property Remodeled', color='green', marker='o')
plt.xlabel('Property Index (Least 50 Lowest Total Property Value)')
plt.ylabel('Year')
plt.title('Property Built vs Property Remodeled for Least 50 Lowest Total Property Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)  # Add grid lines for better readability

# Show plot
plt.tight_layout()
plt.show()
