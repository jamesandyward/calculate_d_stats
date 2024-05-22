# D statistics pipeline

These are a series of scripts I have made to automate a lot of the steps needed to calculate D statistics for a large set of data.

# Step 1 

We start off with a set of PLINK files. The first thing you will have to do is fix the last column in the .fam file. Typically it is set to -9, but this causes problems downstream of this pipeline. So best to fix it now. 

You can do this with this line. Just copy the contents of the new file to the old one. 
```
  awk '{$NF=1}1' input_file.fam > output_file.fam
```
# Step 2

The next thing we want to do is generate population files for each of the populations we want to calculate D statistics for. This is the purpose of the gen_pop.py file. To do this we need to generate a few input files. 

The first file we need to make is the dstats.pop.file. This file contains the individual samples we intend to use as the reference pops when calculating the D statistics. So PopA, PopC and Out. The format of this file is tab separated and should have two columns. The first should have the family ID and the second should have the individual ID. These can be easily extracted from the .fam file. 

The next input file we need is the breeds.txt file, or whatever you wish to name it, this file contains all of the populations you want to calculate D statistics for. This is just a single column of data and it should just have the family ID. It doesn't matter if there are duplicates the gen_pop.py script will remove them. 

Running gen_pop.py will generate a folder which will contain text files that have the family ID and individual ID of the breeds we want to calculate D statistics for, as well as the reference populations from the dstats.pop.file.

# Step 3

The next thing we want to do is to generate the equations we want to run using ADMIXTOOLS and you can do this using the equation_file.py. I have made it do that equation files are generated for each each of the breeds. To do this we need to provide some input files. These are very straightforward. The first file we need to provide is the PopA.txt file, which contains the individual ID for the individual we wish to use as PopA, similarly we need to provide one for PopC and the outgroup, Out. This script will generate a folder with the equations as text files and are correctly formatted for ADMIXTOOLS. 

# Step 4

The next thing we will have to generate eigensoft files for each of the populations of interest. You can do this using plink2eigensoft.py. This script first creates PLINK files of the population of interest, then converts that set of PLINK files into eigensoft format. It then removes the PLINK files it generated. Leaving you with a set of eigensoft files for each of your breeds. While it might seem like a lot of work, splitting your dataset up like this is standard as it would be too computationally intensive to calculate D statistics on a very large dataset numbering in the hundreds. You simply have to give it the prefix of your plink file and the folder we generated earlier that contains the population files. Like so:

```
  python3 plink2eigensoft.py myplinkfile popfiles/
```
# Step 5

The final step here is to generate the D statistics themselves. We can do this using the CalculateDstats.py script. We only need to provide it with three things, the popfiles directory, the equations directory and the bash script to run ADMIXTOOLS. This will output the D statistics for each of the populations we specified and for the equations we gave it. 
