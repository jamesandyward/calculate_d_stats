import os
import subprocess
import sys

def modify_control_labels(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Apply the modifications to replace 'Control' with the part of the label after ':'
        updated_lines = []
        for line in lines:
            if 'Control' in line:
                label_part = line.split(':')[1].split()[0]  # Get the part of the label after ':' and before 'U'
                updated_line = line.replace('Control', label_part)
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)

        # Write the updated content to the same file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"File updated successfully. Updated file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_pipeline_for_population(prefix, population_file):
    eigensoft_dir = 'eigensoft'
    popfiles_dir = 'popfiles'

    # Ensure directories exist
    os.makedirs(eigensoft_dir, exist_ok=True)

    # Extract basename for population
    population = os.path.basename(population_file).split('.')[0]

    # Step 1: Run plink2 for the population
    plink_output_prefix = os.path.join(eigensoft_dir, population)
    subprocess.run(f'plink2 --bfile {prefix} --cow --allow-extra-chr --keep {population_file} --make-bed -out {plink_output_prefix}', shell=True)

    # Step 2: Convert PLINK files to EIGENSOFT format
    subprocess.run(f'./convertf.sh {plink_output_prefix}', shell=True)

    # Step 3: Edit .ind file using the integrated modify_control_labels function
    ind_file_path = f'{plink_output_prefix}.ind'
    modify_control_labels(ind_file_path)

    # Step 4: Delete the newly created PLINK files
    for extension in ['.bed', '.bim', '.fam']:
        os.remove(f'{plink_output_prefix}{extension}')

    print(f"Pipeline execution completed for population: {population}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pipeline.py <plink_prefix> <path_to_population_file>")
        sys.exit(1)
    
    prefix = sys.argv[1]
    pop_file_path = sys.argv[2]

    # Process each population file
    if os.path.isdir(pop_file_path):
        for popfile in os.listdir(pop_file_path):
            full_path = os.path.join(pop_file_path, popfile)
            if os.path.isfile(full_path):
                run_pipeline_for_population(prefix, full_path)
    else:
        run_pipeline_for_population(prefix, pop_file_path)
