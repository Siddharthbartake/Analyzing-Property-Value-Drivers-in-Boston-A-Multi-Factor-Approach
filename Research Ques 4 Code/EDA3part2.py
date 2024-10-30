import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Filter out rows with missing values in 'Building Value' or 'Total Property Value'
filtered_data = data.dropna(subset=['Building Value', 'Total Property Value'])

# Group data by 'Building Value' and calculate the mean 'Total Property Value' for each 'Building Value'
building_value_mean = filtered_data.groupby('Building Value')['Total Property Value'].mean().reset_index()

# Plotting the relationship between 'Building Value' and 'Total Property Value' using a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(data=building_value_mean, x='Building Value', y='Total Property Value', color='skyblue')
plt.title('Relationship between Building Value and Total Property Value')
plt.xlabel('Building Value')
plt.ylabel('Average Total Property Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
