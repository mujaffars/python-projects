import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('students_scores.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Calculate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Add a new column for the average score
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Display the DataFrame with the new 'Average' column
print("\nDataFrame with Average Scores:")
print(df)

# Find the student with the highest average score
top_student = df.loc[df['Average'].idxmax()]
print("\nStudent with the Highest Average Score:")
print(top_student)