import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Select relevant columns
selected_columns = ['Crime Incident Year', 'Crime Neighborhood', 'School Zipcode', 'School ID', 'Property Built', 'Total Property Value']
property_data = data[selected_columns]

# Label encoding for 'Crime Neighborhood'
label_encoder = LabelEncoder()
property_data['Crime Neighborhood'] = label_encoder.fit_transform(property_data['Crime Neighborhood'])

# Calculate correlations
correlation_matrix = property_data.corr()['Total Property Value'].drop('Total Property Value')

# Plotting correlation coefficients
plt.figure(figsize=(8, 6))
correlation_matrix.plot(kind='bar', color='skyblue')
plt.title('Correlation with Total Property Value')
plt.xlabel('Variable')
plt.ylabel('Correlation Coefficient')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
