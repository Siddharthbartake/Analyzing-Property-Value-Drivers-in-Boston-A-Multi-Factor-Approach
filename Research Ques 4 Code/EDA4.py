import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Filter out rows with missing values in 'Land Value' or 'Total Property Value'
filtered_data = data.dropna(subset=['Land Value', 'Total Property Value'])

# Get the top 5 unique estate addresses based on frequency
top_estate_addresses = filtered_data['Estate Address'].value_counts().nlargest(6).index.tolist()
top_estate_addresses = [address for address in top_estate_addresses if address]

# Plotting the relationship between 'Land Value' and 'Total Property Value' using a bubble plot
plt.figure(figsize=(10, 6))
for address in top_estate_addresses:
    estate_data = filtered_data[filtered_data['Estate Address'] == address]
    plt.scatter(estate_data['Land Value'], estate_data['Total Property Value'], s=50, alpha=0.5, label=address)

# Setting labels and title
plt.xlabel('Land Value')
plt.ylabel('Total Property Value')
plt.title('Relationship between Land Value and Total Property Value')
plt.legend(title='Top 5 Estate Addresses', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)  # Add grid lines for better readability
plt.tight_layout()

# Show plot
plt.show()
