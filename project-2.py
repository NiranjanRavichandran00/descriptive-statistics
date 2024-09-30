"""
    Study Group: Standard Deviants 
    Names: Niranjan Ravichandran
           Arjun Venkat
           Sanjith Chockan
           Akshay Jagadeesh
           Nikita Sanjay khachane
           Nikita Ramachandran
    Language: Python 
    Version: 3.11.4
"""
import numpy as np
import random

def find_parameters(datapoints):
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

# Read and store the data from the text file
def read_datapoints_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()  
        datapoints = list(map(int, data.split(',')))
    return datapoints

def find_parameters_sample(datapoints):
    # Use different variable names to avoid conflict with built-in functions
    length = len(datapoints)
    min_value = min(datapoints)
    max_value = max(datapoints)
    mean = sum(datapoints) / length
    variance = sum((x - mean) ** 2 for x in datapoints) / (length-1)  # N-1 is used for sample variance
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

def generate_sample(num_samples, datapoints):
    random_indices = set()

    while len(random_indices) < num_samples:
        random_index = random.randint(0, len(datapoints)-1)
        if random_index not in random_indices:
            random_indices.add(random_index)
        
        #print(random_indices)
    
    new_sample = []
    for index in random_indices:
        new_sample.append(datapoints[index])
    
    return new_sample

file_path = 'large.txt'  
datapoints = read_datapoints_from_file(file_path)
find_parameters(datapoints)

#sample of 1/1000 the size
sample_1000th = generate_sample(len(datapoints)/1000, datapoints)
find_parameters_sample(sample_1000th)
print("------------------------------")
#sample of 1/100 the size
sample_100th = generate_sample(len(datapoints)/100, datapoints)
find_parameters_sample(sample_100th)
print("------------------------------")
#sample of 1/10 the size
sample_10th = generate_sample(len(datapoints)/10, datapoints)
find_parameters_sample(sample_10th)


