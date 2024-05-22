import os
import pandas as pd
import csv

def process_file(input_file_path, output_file_path):
    # Initialize a list to hold the extracted results
    extracted_results = []

    # Read the input file
    with open(input_file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line starts with 'result:'
            if line.startswith('result:'):
                # Strip leading 'result:' and any leading/trailing whitespace, then split the line into fields
                data_fields = line.strip().replace('result:', '').split()
                # Append the data fields to the list of extracted results
                extracted_results.append(data_fields[:-1])  # Exclude the last column

    # Define the column names
    column_names = ['Popa', 'Popb', 'Popc (Source population)', 'Popd (out group)', 'D stat', 'Z score', 'BABA', 'ABBA']

    # Convert the extracted data into a DataFrame
    df = pd.DataFrame(extracted_results, columns=column_names)

    # Write the DataFrame to a CSV file
    df.to_csv(output_file_path, index=False)

# Directory containing the input text files
directory_path = 'Dstats/'

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Construct the full file paths
        input_file_path = os.path.join(directory_path, filename)
        output_file_path = os.path.join(directory_path, filename.replace('.txt', '.csv'))
        
        # Process the file and write the results to a CSV
        process_file(input_file_path, output_file_path)
        print(f'Processed {input_file_path} and saved results to {output_file_path}')
