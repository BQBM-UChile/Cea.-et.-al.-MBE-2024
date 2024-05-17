import os
import numpy as np

# Directory containing the data files
data_directory = os.getcwd()

# Initialize a dictionary to store filename-distance pairs
file_distance_dict = {}

# Recursively iterate through files in the directory and subdirectories
for root, dirs, files in os.walk(data_directory):
    # Filter subdirectories that start with "rep"
    dirs[:] = [d for d in dirs if d.startswith("rep")]
    
    for filename in files:
        if filename.endswith(".dat"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                data = [(int(line.split()[0]), float(line.split()[1])) for line in lines]
                
                # Extract distances for calculation
                distances = [distance for frame, distance in data]
                                               
                # Count frames meeting the criteria
                count_distance_less_than_4_5 = sum(1 for distance in distances if distance <= 4.5)
                
                # Calculate the percentage
                percentage_distance_less_than_4_5 = (count_distance_less_than_4_5 / 60000) * 100
                
                # Store filename and percentage in the dictionary if percentage is 10% or more
                if percentage_distance_less_than_4_5 >= 10:
                    file_distance_dict[filename] = percentage_distance_less_than_4_5

# Print the filenames and corresponding percentages
for filename, percentage in file_distance_dict.items():
    print(f"File: {filename}, Percentage: {percentage:.2f}%")

