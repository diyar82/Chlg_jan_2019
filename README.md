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

1.	The Run function is Linux/Bash
2.	The Run function looks in to the input file. If the input file was short, Bash will direct it to Python3 pharmacy_counting.py directly
3.	If the input file was long, Bash will first sort the data according to drug name. Though sorting is costy (Varies between nlogn to n^2). It is way more effecient to sort at the start than to look through the document for same drug name. Then each data file is dealt with saparetly by Python long_pharmacy_counting.py
4. 	The python3 program uses no libraries (No NumPy or Pandas) except for sys to read varible pushed by Linux/bash program.
5.	The data read and divided into variables and stored in a matrix.
6.	Though this doesn’t seem to be efficient but it is the only way to compare the data efficiently.
7.	The total unique prescribers are the total number mines the repeating ones
8.	The total drug expenditure is the sum of individual expenditures of the array for same drug name
9.	All data are stored in another matrix to resort it according to the total expenditure

