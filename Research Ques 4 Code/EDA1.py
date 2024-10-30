import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from Excel
data = pd.read_excel('Final Blend.xlsx')

# Group data by 'Crime Neighborhood' and count the number of occurrences of 'Crime Incident Number'
crime_counts = data.groupby('Crime Neighborhood')['Crime Incident No.'].count().reset_index()

# Plotting the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=crime_counts, x='Crime Neighborhood', y='Crime Incident No.', color='skyblue')
plt.title('Number of Crime Incidents in Each Crime Neighborhood')
plt.xlabel('Crime Neighborhood')
plt.ylabel('Number of Crime Incidents')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
