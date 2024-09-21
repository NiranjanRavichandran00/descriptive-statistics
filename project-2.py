import numpy as np

# Read and store the data from the text file
def read_datapoints_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()  
        datapoints = list(map(int, data.split(',')))
    return datapoints

file_path = 'small.txt'  
datapoints = read_datapoints_from_file(file_path)

# Use different variable names to avoid conflict with built-in functions
length = len(datapoints)
min_value = min(datapoints)
max_value = max(datapoints)
mean = sum(datapoints) / length
variance = sum((x - mean) ** 2 for x in datapoints) / length  # N is used for population variance
std_dev = variance ** 0.5

# Calculate quartiles, interquartile range, and outliers
def calculate_outliers(datapoints):
    q1 = np.percentile(datapoints, 25)
    q3 = np.percentile(datapoints, 75)
    iqr = q3 - q1  # Interquartile range
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in datapoints if x < lower_bound or x > upper_bound]
    
    return q1, q3, iqr, len(outliers)

q1, q3, iqr, outlier_count = calculate_outliers(datapoints)

# Print the results
print("Length: " + str(length))
print("Minimum: " + str(min_value))
print("Maximum: " + str(max_value))
print("Mean: " + str(mean))
print("Variance: " + str(variance))
print("STDEV: " + str(std_dev))
print(f"25% Quartile: {q1}")
print(f"75% Quartile: {q3}")
print(f"Interquartile Range: {iqr}")
print(f"{outlier_count} outliers found.")