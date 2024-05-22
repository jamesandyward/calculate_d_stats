import os
import subprocess
import sys

# Directory paths
popfiles_dir = 'popfiles/'
equations_dir = 'equations/'
runqpDstat_script_path = './runqpDstat.sh'
print(runqpDstat_script_path)  # Add this line to debug the path


# Function to run D statistics for a specific population
def run_d_statistics_for_population(population_name, popfiles_dir, equations_dir, runqpDstat_script_path):
    filepath = os.path.join(popfiles_dir, f'{population_name}.txt')
    if os.path.isfile(filepath):
        equation_file_path = os.path.join(equations_dir, f'{population_name}.txt')
        # Check if the corresponding equation file exists
        if os.path.isfile(equation_file_path):
            # Call the runqpDstat.sh script with the population name and the equation file
            subprocess.run([runqpDstat_script_path, population_name], shell=True)
        else:
            print(f"Equation file for {population_name} not found.")
    else:
        print(f"Population file for {population_name} not found.")

# Check if a specific population is provided as a command-line argument
if len(sys.argv) > 1:
    specific_population = sys.argv[1]
    run_d_statistics_for_population(specific_population, popfiles_dir, equations_dir, runqpDstat_script_path)
else:
    # Iterate over files in the popfiles directory to process the entire dataset
    for filename in os.listdir(popfiles_dir):
        if os.path.isfile(os.path.join(popfiles_dir, filename)):
            population_name = os.path.splitext(filename)[0]
            run_d_statistics_for_population(population_name, popfiles_dir, equations_dir, runqpDstat_script_path)

print("D statistics calculation completed.")
