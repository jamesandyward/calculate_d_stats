import os

# Function to read the entire content of a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def generate_equations_with_processed_popfiles(popa, popc, out, popfiles_dir, equation_format, equations_dir):
    os.makedirs(equations_dir, exist_ok=True)  # Ensure the equations directory exists

    popa_list = set(popa.strip().split('\n'))
    popc_list = set(popc.strip().split('\n'))
    out_population = out.strip().split('\n')[0]  # Assuming only one 'out' population

    # Iterate over files in the popfiles directory
    for filename in os.listdir(popfiles_dir):
        filepath = os.path.join(popfiles_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                popb_individuals = set(line.strip().split('\t')[1] for line in file if line.strip() != '')
            popb_individuals -= (popa_list | popc_list | {out_population})

            # File to store all equations for this popB
            equation_file_path = os.path.join(equations_dir, f'{os.path.splitext(filename)[0]}.txt')

            with open(equation_file_path, 'w') as file:
                for popa_individual in popa_list:
                    for popc_individual in popc_list:
                        for popb_individual in popb_individuals:
                            equation = equation_format.replace('POPA', popa_individual).replace('POP1', popb_individual).replace('POPC', popc_individual).replace('OUT', out_population)
                            file.write(equation + '\n')

# Paths and contents (replace with actual values)
popa_file_path = 'PopA.txt'
popc_file_path = 'PopC.txt'
out_file_path = 'Out.txt'
popfiles_dir = 'popfiles'
equations_dir = 'equations'

# Read file contents
popa_content = read_file(popa_file_path)
popc_content = read_file(popc_file_path)
out_content = read_file(out_file_path)

equation_file_content = 'POPA\tPOP1 \tPOPC\tOUT'  # Replace with actual format

# Generate equations
generate_equations_with_processed_popfiles(popa_content, popc_content, out_content, popfiles_dir, equation_file_content, equations_dir)

print(f'Equations have been generated in {equations_dir}')
