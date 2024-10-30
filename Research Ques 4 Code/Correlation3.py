import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Select relevant columns
selected_columns = ['School Zipcode', 'Crime Incident No.', 'Crime Zipcode',
                    'Crime Incident Year', 'Land Value', 'Building Value',
                    'Gross Tax', 'Property Built', 'Estate Street Number',
                    'Total Property Value']

property_data = data[selected_columns]

# Check for non-numeric values in relevant columns
for column in selected_columns:
    non_numeric_values = property_data[column][~pd.to_numeric(property_data[column], errors='coerce').notnull()]
    if not non_numeric_values.empty:
        print(f"Non-numeric values found in column '{column}': {non_numeric_values.unique()}")

# Convert columns to numeric, replacing non-convertible values with NaN
property_data = property_data.apply(pd.to_numeric, errors='coerce')

# Drop rows with NaN values, assuming NaN represents missing data
property_data.dropna(subset=selected_columns, inplace=True)

# Calculate correlations
correlation_matrix = property_data.corr()['Total Property Value'].drop('Total Property Value')

# Plotting correlation coefficients
plt.figure(figsize=(10, 6))
correlation_matrix.plot(kind='bar', color='skyblue')
plt.title('Correlation with Total Property Value')
plt.xlabel('Variable')
plt.ylabel('Correlation Coefficient')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting scatter plots to explore relationships
plt.figure(figsize=(12, 8))

for i, column in enumerate(property_data.columns[:-1]):  # Exclude 'Total Property Value'
    plt.subplot(3, 3, i+1)
    sns.scatterplot(data=property_data, x=column, y='Total Property Value', color='skyblue')
    plt.title(f'{column} vs Total Property Value')
    plt.xlabel(column)
    plt.ylabel('Total Property Value')

plt.tight_layout()
plt.show()
