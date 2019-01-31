path='./input/itcont.txt'   				## Path to input file
reader = open(path,'r')     				## Read the file
lines=reader.readlines()    				## Definig a varible for each line
reader.close()              				## Finshed reading the file so close it
total_entry=len(lines)                			## To find the length of the file
sorted_data = [[0,0,0,0,0] for y in range(total_entry)] ## We SOON sort the data by DRUG NAME
for i in range (total_entry):         			## This loop is for assigning the data to our varibles
    sorted_data[i]=lines[i].split(",")   		## this (ideally) gives us an 5 by N matrix
lines=None                  				## Nullify to clean RAM space

sorted_data.sort(key=lambda x:x[3])  			## The data sorted by repeated DRUG NAME

repeated_drug_count=1                     		## Adding a counter
first_same_drug =0                    			## Setting a start point
output_data = []                			## Output matrix needed in the next loop
less_total_entry=total_entry-1                       	## Assgin varible used in the next loop 
for i in range (less_total_entry):        	 	## Loop through the Data
    if sorted_data[i][3] == sorted_data[i+1][3]:  	## Find out where the drug name changed
        repeated_drug_count +=1                       	## Each time the drug name is same we add to the counter
    else:
        repeated_prescriber = 0                    	## Nothing repeating so far
        last_same_drug = first_same_drug + repeated_drug_count	## The range of a specific drug name
        if repeated_drug_count > 1:                   	## If a drug prescribed more than 1 time
            less_last_same = last_same_drug -1            	## Assgin varible used in the next loop
            for k in range (first_same_drug,less_last_same): 	## This loop is to compare all elements to find repeating prescribers 
                next_repeated_drug = k+1        		##
                for m in range(next_repeated_drug,last_same_drug):  ## last same drug is not compared and has next drug name
                    if sorted_data[k][1] == sorted_data[m][1] and sorted_data[k][2] == sorted_data[m][2]:   ## Compare name and surname
                        repeated_prescriber +=1    	## Count drug prescribed by same name & surname  
        total_money = 0.0                     		## Varible (float) for total money spend 
        for j in range (first_same_drug,last_same_drug):## last same drug is where drug name changed and loops stop 
            total_money +=float(sorted_data[j][-1])    	## This loop to count the total money spend on a specific drug
        total_money=int(round(total_money))           	## Taking the rounded integer part of the number

        output_data.append([sorted_data[first_same_drug][3],repeated_drug_count-repeated_prescriber,total_money])
 
        repeated_drug_count = 1				## Resetting the counter to 1	
        first_same_drug = last_same_drug                ## last same drug is where drug name changed and loops stop
sorted_data=None                             		## Nullify to clean RAM space
output_data.sort(key=lambda x:x[2],reverse=True)    	## Sort for higher number at top
output_length=len(output_data)                      	##
f= open("./output/top_cost_drug.txt","w+")      	## Writing the data to output File
print("drug_name,num_prescriber,total_cost", file=f)    ##
for i in range (output_length):                		##
    print(output_data[i][0],output_data[i][1],output_data[i][2],sep=",", file=f)    ##
f.close()                               		##
output_data=None                            		## Clean the mess

