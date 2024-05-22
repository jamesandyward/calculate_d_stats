#!/bin/bash

dir="eigensoft"

mkdir Dstats

# Loop through .txt files in the directory
for file_path in "$dir"/*.geno; do
    if [ -f "$file_path" ]; then
        # Extract filename with extension
        file_with_extension=$(basename "$file_path")
        
        # Remove the '.txt' extension to get only the prefix
        in1="${file_with_extension%.geno}"

        # Run qpDstat command with the prefix
        qpDstat -p <(echo "genotypename:       eigensoft/${in1}.geno
        snpname:        eigensoft/${in1}.snp
        indivname:      eigensoft/${in1}.ind
        popfilename:        equations/${in1}.txt") > Dstats/${in1}_Dstats.txt
    fi
done
