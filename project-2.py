# Read and store the data from the text file
def read_datapoints_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()  
        datapoints = list(map(int, data.split(',')))
    return datapoints


file_path = 'small.txt'  
datapoints = read_datapoints_from_file(file_path)

# Print the datapoints
print(datapoints)
print(len(datapoints))