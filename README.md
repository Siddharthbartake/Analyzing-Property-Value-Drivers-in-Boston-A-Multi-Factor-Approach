# Analyzing-Property-Value-Drivers-in-Boston-A-Multi-Factor-Approach

### For the entire Data Analysis, refer to [ISDS577]([path/to/your/file.extension](https://github.com/Siddharthbartake/Analyzing-Property-Value-Drivers-in-Boston-A-Multi-Factor-Approach/blob/main/ISDS577Project.pdf))
### Overview
This project presents an in-depth analysis of Boston's real estate market, utilizing a dataset integrating property, public school, and crime data for the city. Our goal was to explore the factors influencing property values across various neighborhoods in Boston, with a focus on actionable insights for real estate investors and city planners.

### Project Details

- **Course**: ISDS 577 - Data Analytics
- **Contributors**: Ananya Rattani, Siddharth Mahesh Bartake
- **Dataset**: Comprises 61,741 rows and 47 variables, sourced from [Kaggle](https://www.kaggle.com/datasets/crawford/boston-public-schools), [data.boston.gov](https://data.boston.gov/dataset/property-assessment/resource/695a8596-5458-442b-a017-7cd72471aade), and [Boston PD Crime Hub](https://boston-pd-crime-hub-boston.hub.arcgis.com/datasets/).

### Data Collection and Processing

1. **Data Sources**: We integrated three datasets—Boston public school, property assessment, and crime data—based on common zip codes.
2. **Preprocessing**: Data cleaning was performed in Alteryx, addressing missing values and outliers. Merged datasets were then exported for analysis.
3. **Tools Used**: Python, Excel, Alteryx, and Tableau.

### Research Questions

1. **How do property features impact value?**
2. **What is the relationship between property age and value?**
3. **How are taxes and crime rates correlated?**
4. **What are the trends in property prices over time?**
5. **Can we predict property prices based on various factors?**
6. **What are the key drivers of property value across neighborhoods?**

### Methodology

- **Statistical Analysis**: Descriptive statistics, correlation matrices, and regression models were applied to understand relationships between variables.
- **Machine Learning Models**:
  - *Linear Regression*: Baseline model with moderate predictive power.
  - *Random Forest Regression*: Achieved higher accuracy (R² = 0.9223).
  - *CART (Classification and Regression Trees)*: Best-performing model with R² = 0.987.
- **Visualization**: Scatter plots, heatmaps, and geographical maps were created to illustrate relationships and trends.

### Key Findings

1. **Property Features & Value**: Bedrooms, bathrooms, floors, and exterior materials like brick and vinyl positively influence property value.
2. **Property Age**: Older properties tend to retain value better, with remodeled properties showing slight depreciation.
3. **Crime & Tax Correlation**: A moderate negative correlation exists between crime rates and property taxes; areas with higher taxes tend to have lower crime rates.
4. **Geographic Trends**: Central neighborhoods like Back Bay and Beacon Hill have higher property values, while outer neighborhoods show lower averages.
5. **Predictive Modeling**: Key predictors of property value include gross tax, building value, and land value.
6. **Investment Recommendations**:
   - Prioritize high-security neighborhoods with low crime rates.
   - Focus on properties with high building and land values.
   - Invest in renovations for long-term property appreciation.

### Conclusion
This analysis provides insights into the Boston real estate market, highlighting factors that influence property values, crime rate impacts, and the importance of location. The predictive models indicate significant potential for gross tax, building, and land values to predict property prices, suggesting investment strategies tailored to these variables.

### Future Work
Further research could incorporate time series analysis for dynamic property value trends and GIS data for enhanced spatial analysis.

### How to Use
Clone the repository and open the analysis scripts in Jupyter Notebook or your preferred Python environment. Visualizations are available in Tableau and can be accessed via shared links in the repository.

---

This project equips real estate investors and city planners with a data-driven approach to understanding Boston’s property market, enabling informed decision-making and strategic investments.

---

### License
This project is licensed under the MIT License - see the LICENSE file for details.
