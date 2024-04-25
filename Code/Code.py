# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df= pd.read_csv(r'E:\Study\UH\Data Handling and Visualisation\vgsales.csv')
df.head()

df.describe()

df.info()
# Select only numeric columns
numeric_columns = df.select_dtypes(include=['number'])

# Calculate mean, median, standard deviation, skewness, and kurtosis
statistics = numeric_columns.agg(['mean', 'median', 'std', 'skew', 'kurt'])

# Compute the correlation matrix
correlation_matrix = numeric_columns.corr()

# Get basic statistics using describe()
basic_statistics = numeric_columns.describe()

# Print the results
print("Mean, Median, Standard Deviation, Skewness, Kurtosis:")
print(statistics)

print("\nCorrelation Matrix:")
print(correlation_matrix)

print("\nBasic Statistics:")
print(basic_statistics)


#creating scatter Plot
def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], alpha=0.5)
    plt.title(f'Scatter Plot of {y_column} vs {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.show()



# Plot usage
plot_scatter(df, 'Year', 'Global_Sales')

#creating Bar Graph
def plot_top_platforms(df, n=20):
    top_platforms = df['Platform'].value_counts().nlargest(n)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_platforms.values, y=top_platforms.index, hue=top_platforms.index, palette='viridis', dodge=False, legend=False)
    plt.title(f'Top {n} Platforms by Number of Games')
    plt.xlabel('Number of Games')
    plt.ylabel('Platform')
    plt.show()

# Plot usage
plot_top_platforms(df)

#Creating Correlation Heatmap
def plot_correlation_heatmap(df):
    # Select only numerical columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Calculate correlation matrix
    corr = numeric_df.corr()

    # Create a heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()


# Plot usage
plot_correlation_heatmap(df)
