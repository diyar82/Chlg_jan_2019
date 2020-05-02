#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from itertools import permutations 
##############################################
### N = 10 , 10! = ‭3,628,800‬ , Solvable analytically
##############################################

### Since every configuration is equiprobable every configuration is counted

##############################################
l = list(permutations(range(1, 11))) 
total_gt_44=0
newarry = list()
for i in range(len(l)):
    sum=0
    sum+=l[i][0]
    m=len(l[0])-1
    for j in range(m):
        sum+=abs(l[i][j]-l[i][j+1])
    newarry.append(sum)
    if sum > 44:
        total_gt_44+=1
print (" the mean of your total payment for N=10 is "+ str(np.mean(newarry)))
print (" the standard deviation of your total payment for N=10 is " + str(np.std(newarry)))
print (" the probability that your total payment is greater than or equal to 45 for N=10 " + str(total_gt_44/len(newarry)))
l = None
##############################################
### N = 20 , 20! = ‭2,432,902,008,176,640,000‬ , Not Solvable analytically
##############################################

### 100M samples are taken to make enough data to make an educated quess 

##############################################
Payments= []
Deviations= []
Prob_160= []
Loop1=int(1000)
loop2=int(100000)

for itera in range(Loop1):
    total_gt_160=0
    totalsum=0
    in_Array= list()
    for i in range(loop2):
        arr = list(range(1,21))
        old_value=0
        sum=0
        for j in range(20):
            random_index = np.random.randint(len(arr))
            value = arr.pop(random_index)
            sum=sum+abs(value-old_value)
            old_value=value
        in_Array.append(sum)
        if sum > 160:
            total_gt_160+=1
        totalsum=totalsum+sum
    totalsum=totalsum/loop2
    Payments.append(totalsum)
    Deviations.append(np.std(in_Array))
    Prob_160.append(total_gt_160/loop2)
    
Pay_Expect= np.mean(Payments)
Dev_Expect= np.mean(Deviations)
Prob_160_Expect = np.mean(Prob_160)

print (" the mean of your total payment for N=20 is "+ str(Pay_Expect))
print (" the standard deviation of your total payment for N=20 is " + str(Dev_Expect))
print (" the probability that your total payment is greater than or equal to 160 given N=20 is " + str(Prob_160_Expect))


# In[3]:





# In[ ]:




