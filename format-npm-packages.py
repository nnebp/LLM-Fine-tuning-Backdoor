def extract_package_names(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            start = line.find('[') + 1
            end = line.find(']')
            package_name = line[start:end]
            outfile.write(package_name + '\n')

input_file_path = './unformatted-npm-packages.txt'  # Replace with the actual input file path
output_file_path = './formatted-npm-packages.txt'  # Replace with the desired output file path

# Uncomment the line below to run the script with the specified file paths
extract_package_names(input_file_path, output_file_path)
