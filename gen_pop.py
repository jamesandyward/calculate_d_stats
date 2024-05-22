import shutil
import os
from collections import defaultdict

fam_file_path = '../dataset_updated_ids.fam' 
pop_file_path = 'dstats.pop.file' # Extra pops to include for calculating D stats
famid_list_file_path = 'breeds.txt' # Breeds to select from the fam file 
output_dir = 'popfiles/' # Output directory


# Function to remove duplicates from the FAMID list
def process_files_with_famid_list(fam_file_path, pop_file_path, famid_list_file_path, output_dir):
    # Create a directory for the output files if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the .fam file and store FAMID and IID in a dictionary
    with open(fam_file_path, 'r') as fam_file:
        fam_dict = defaultdict(list)
        for line in fam_file:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                famid, iid = parts[0], parts[1]
                fam_dict[famid].append(iid)

    # Read the list of FAMIDs from the provided text file and remove duplicates
    with open(famid_list_file_path, 'r') as famid_file:
        famid_list = set(line.strip() for line in famid_file)

    # Read the .pop file and store its contents
    with open(pop_file_path, 'r') as pop_file:
        pop_contents = pop_file.readlines()

    # Write the FAMID and IID pairs to their respective files and append .pop file contents
    for famid in famid_list:
        if famid in fam_dict:
            with open(os.path.join(output_dir, f'{famid}.txt'), 'w') as out_file:
                for iid in fam_dict[famid]:
                    out_file.write(f'{famid}\t{iid}\n')
                out_file.writelines(pop_contents)

    return f'Files created in {output_dir}'

# Call the function with the new parameters
process_files_with_famid_list(fam_file_path, pop_file_path, famid_list_file_path, output_dir)
