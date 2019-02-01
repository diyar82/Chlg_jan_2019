This is a program written for Insight Data Engineering - Coding Challenge Jan/2019
The program is written by Diyar Jamal (diyar82@gmail.com). feel free to use one part or the entire program for any reason (Common Commerce)

# Table of Contents
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [Output](README.md#output)
4. [Approach](README.md#Approach)


# Problem
You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name. 

# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions listed by drug name and the cost of the medication. 

# Output 

The program creates a file `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

# Approach

1.	The Run function "Using ./run.sh" makes Linux/bash program run. (Please refer to the flowchart)
2. 	If the total line number of the Input file itcont.txt < 1M lines the problem can directly be solved by run pharmacy_counting.py     written In Python 3 (go to 10 for details)
3.	If the input file was long, Bash will first Clean the data to avoid unwanted errors such as having "," in a name or surname in the input file.
4.	Sort the data according to drug name. Though sorting is costly (Varies between nlogn to n^2). It is way more efficient to sort at the start than to look through the document for same drug name.
5. 	Divide itcont.txt into smaller files (Example Divide 243M entry to 243 smaller files each with 1M entry) so it does not kill the RAM while reading and splitting lines in Python. (The default is 1M can be changed by changing acceptable_range=1000000 variable)
6. 	Run python3 long_pharmacy_counting.py and provide the input file count
7. 	long_pharmacy_counting.py is similar to pharmacy_counting.py except it get multiple sorted files and has multiple output files
8. 	Bash Concatenates the output files into a single file then sort them according to the highest total drug expenditure 
9. 	Bash then edit to the final format and heading tas required by the challenge question 
10. Regarding The python3 program (pharmacy_counting.py, long_pharmacy_counting.py), they use no libraries (No NumPy or Pandas) except for sys to read variable pushed by Linux/bash program. (Please look at the flow chart)
11.	The pharmacy_counting.py read the data directly from itcont.txt and divide it into variables and stored in a matrix.
12.	Though this doesn’t seem to be efficient (RAM wise) but it is a fast way to compare the data as the data is small.
13.	pharmacy_counting.py finds the range where the drug has same name and name the range as repeated_drug_count
14.	pharmacy_counting.py looks further through the repeated drug range to find the repeated prescribers. The number of repeated prescribers is stored in repeated_prescriber varible
15.	The number of unique prescribers is the total number of a specific drug being prescribed minus the number of repeated prescribers
16.	The total amount of money spend on any drug is the sum of all price entries having same drug name.
17.	The data is stored and pharmacy_counting.py moves on to the next drug name.
18.	Once the data collected it is sorted according to descending total amount
19.	The sorted data is stored in a file named top_cost_drug.txt
