#!/bin/bash
#
rm ./output/top_cost_drug.txt
file_length=`wc -l <./input/itcont.txt`						## Determine how big the input data is
acceptable_range=1000000							## Depending on the RAM acceptible data range is determined 
if [ $file_length -lt $acceptable_range ]					## If the input file is small use python directly  
then
	python3 ./src/pharmacy_counting.py                                      ## Use Python 3 code to execute the task
									
else										## If the input file is big use divide and conquer technique
	awk -F, 'NF<=5' < ./input/itcont.txt > ./input/cleaned.txt		## Ignore files that have more than 5 fields seperated by (,) 
	sort -k4 -t ',' < ./input/cleaned.txt > ./input/sorted.txt		## Sorting the file at the beggining according to drug name
	rm ./input/cleaned.txt							## Remove unwanted files(This can be reduced to one step through "|")
        file_number=$(($file_length/$acceptable_range))				## Determine number of smaller data files
        for ((i=0; i<=file_number; i++))					## The loop divides the huge drug sorted file over smaller files
                do									
                        file_start=$(((($i)*$acceptable_range)+1))
                        file_end=$(((($i+1)*$acceptable_range)))
                        sed -n ''$file_start', '$file_end'p' ./input/sorted.txt > ./input/file_$i.txt
		done
	python3 ./src/long_pharmacy_counting.py $file_number			## Calling Python code to execute the input files
	wait									## Waiting for python code to finish 
	sed -i '$ d' ./output/top_cost_drug_$file_number.txt			## The very last output is removed because it is the residue
	for i in $(seq 0 $file_number); do cat ./output/top_cost_drug_$i.txt >> ./output/All_output.txt; done	## Collect the output in a single file
	for i in $(seq 0 $file_number); do rm ./input/file_$i.txt ./output/top_cost_drug_$i.txt ; done		## Clean unwanted files
	sort -t"," -nr -k 3,3 -k 1,1 < ./output/All_output.txt > ./output/top_cost_drug.txt		## Sort output in order of decending drug price
	sed -i '1i\drug_name,num_prescriber,total_cost' ./output/top_cost_drug.txt			## Adding header to the file
	rm ./input/sorted.txt ./output/All_output.txt							## Clean unwanted files
fi


