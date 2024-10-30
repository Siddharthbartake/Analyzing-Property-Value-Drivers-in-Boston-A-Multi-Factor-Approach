import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Remove non-numeric columns that cannot be used for correlation calculation
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# Calculate correlations between all numeric variables and 'Total Property Value'
correlation_matrix = numeric_data.corr()

# Plotting the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap: Numeric Variables vs Total Property Value')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# Show plot
plt.show()
