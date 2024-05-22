import os
import glob
import pandas as pd

# Specify the directory where your CSV files are located
directory_path = 'Dstats/'  # Update this to your directory
output_file_path = 'merged_Indicine_Dstats.csv'

# Get all CSV files in the directory
csv_files = glob.glob(os.path.join(directory_path, '*.csv'))

# Initialize a DataFrame to hold the combined data
combined_data = pd.DataFrame()

# Loop through the list of csv files
for i, file in enumerate(csv_files):
    # Read the current file into a DataFrame
    data = pd.read_csv(file)
    
    # Append the contents of the current file to the combined DataFrame
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_data.to_csv(output_file_path, index=False)

print(f'Merged file saved to {output_file_path}')
