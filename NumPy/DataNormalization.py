import numpy as np

# Create a dataset (array of values)
data = np.array([56, 45, 67, 89, 23, 34, 78, 90, 12, 34, 56])

# Calculate the mean of the data
mean_data = np.mean(data)
print(f"Mean: {mean_data:.2f}")

# Calculate the standard deviation of the data
std_dev_data = np.std(data)
print(f"Standard Deviation: {std_dev_data:.2f}")

# Normalize the data
normalized_data = (data - mean_data) / std_dev_data
print("\nNormalized Data:")
print(normalized_data)
