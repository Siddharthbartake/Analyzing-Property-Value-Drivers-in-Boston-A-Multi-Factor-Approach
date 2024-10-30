import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Filter out rows with missing values in 'Gross Tax' or 'Total Property Value'
filtered_data = data.dropna(subset=['Gross Tax', 'Total Property Value'])

# Plotting Gross Tax vs Total Property Value for each Estate Zipcode
plt.figure(figsize=(12, 8))

sns.scatterplot(data=filtered_data, x='Gross Tax', y='Total Property Value', hue='Estate Zipcode', palette='tab10', alpha=0.7)
plt.title('Impact of Gross Tax on Total Property Value by Estate Zipcode')
plt.xlabel('Gross Tax')
plt.ylabel('Total Property Value')
plt.legend(title='Estate Zipcode', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
