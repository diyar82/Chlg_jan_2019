import sys									## To get the file_number send by Bash
TOTAL_FILES=(int(sys.argv[1])+1)						## The total input files to look through
Remaining_lines=0								## This is the start, no data left from previous files
Residue=[]									## This is the start, no data left from previous files
for i in range (TOTAL_FILES):
	path="./input/file_" + str( i ) + ".txt"				## Read the data files
	reader = open(path,'r')     						##
	lines=reader.readlines()    						## 
	reader.close()              						##
	total_entry=len(lines)							## Get number of read lines
	sorted_data = [[0,0,0,0,0] for y in range(total_entry)]			##
	for j in range(total_entry):                                 		## Split the data that was sorted by drugname (Through bash) 
		sorted_data[j]=lines[j].split(",")                		## -by commas. and save it in a 5xN Matrix
	lines=None								## Clean RAM 
	total_entry=Remaining_lines+total_entry               			## lines left from last input file are added to the data
	sorted_data=Residue+sorted_data						## Residue is the data that is left from last input file
	repeated_drug_count=1							## Each drug starts from 1 and then gets repeated 
	first_same_drug=0							## Setting a start point
	output_data = []                                        		## Output matrix needed in the next loop 
	less_total_entry=total_entry-1						## Assgin varible used in the next loop
	for k in range (less_total_entry):					## Loop through the Data
		if sorted_data[k][-2] == sorted_data[k+1][-2]:        		## Find out where the sorted drug name has changed 
			repeated_drug_count +=1					## Each time the drug name is same we add to the counter
			if (repeated_drug_count+first_same_drug) >= total_entry:	## This is where the iteration hits the end of the data
				Remaining_lines=repeated_drug_count		## These lines can't be processed, the remainig data is in the next file 
				Residue=[]					## An Array to store the remaining information
				for u in range (first_same_drug,total_entry):	## 
					Residue.append(sorted_data[u])	        ## Store the remaining data in the residue                 
				break						## Stop the for loop
		else:
			repeated_prescriber = 0                         	## Nothing repeating so far
			last_same_drug = first_same_drug + repeated_drug_count  ## The range of a specific drug name
			if repeated_drug_count > 1:                     	## If a drug prescribed more than 1 time
				less_last_same = last_same_drug -1              ## Assgin varible used in the next loop
				for l in range (first_same_drug,less_last_same):	## This loop is to compare all elements to find repeating prescribers
					next_repeated_drug = l+1                	## 
					for m in range(next_repeated_drug,last_same_drug):  	## Last same drug is not compared and has next drug nam 
						if sorted_data[l][1] == sorted_data[m][1] and sorted_data[l][2] == sorted_data[m][2]:   ## Compare name and surname
							repeated_prescriber +=1         ## Count drug prescribed by same name & surname 
			total_money = 0.0                               	## Varible (float) for total money spend
			for S in range (first_same_drug,last_same_drug):	## last same drug is where drug name changed and loops stop
				total_money +=float(sorted_data[S][-1])     	## This loop to count the total money spend on a specific drug
			total_money=int(round(total_money))             	## Taking the rounded integer part of the number
#######################################################################################################################################
			output_data.append([sorted_data[first_same_drug][3],repeated_drug_count-repeated_prescriber,total_money])
########################################################################################################################################
####### If a drug prescribed 10 times and 3 of them where repeating prescriber it was prescribed by 7 Unique people     ########
################################################################################################################################
			repeated_drug_count = 1					## Resetting the counter to 1
			first_same_drug = last_same_drug			## last same drug is where drug name changed and loops stop
	sorted_data=None							## Nullify to clean RAM space
	output_length=len(output_data)						##
	f= open("./output/top_cost_drug_" + str( i ) + ".txt","w+")             ## Writing the data to output File
	for q in range (output_length):						##
		    print(output_data[q][0],output_data[q][1],output_data[q][2],sep=",", file=f)    ##
	f.close()                                               		##
	output_data=None							##Clean the mess
