import numpy as np

# Create a NumPy array with temperatures recorded over a week
temperatures = np.array([22.1, 23.5, 19.8, 21.7, 25.0, 20.3, 18.9])

# Calculate the mean temperature
mean_temperature = np.mean(temperatures)
print(f"Mean Temperature: {mean_temperature:.2f}°C")

# Calculate the maximum temperature
max_temperature = np.max(temperatures)
print(f"Maximum Temperature: {max_temperature:.2f}°C")

# Calculate the minimum temperature
min_temperature = np.min(temperatures)
print(f"Minimum Temperature: {min_temperature:.2f}°C")

# Calculate the temperature variance
temperature_variance = np.var(temperatures)
print(f"Temperature Variance: {temperature_variance:.2f}°C²")

# Additional: Calculate the standard deviation
temperature_std_dev = np.std(temperatures)
print(f"Standard Deviation of Temperature: {temperature_std_dev:.2f}°C")