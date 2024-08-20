#https://www.geeksforgeeks.org/counting-sort/
ar=[2,5,3,0,2,3,0,3]
mx=max(ar) #finding the max value from the input array/list
fr=[0]*(mx+1) #initialization of the frequency array
for i in ar: #calculating the frequency
    fr[i]+=1

out=[0]*len(ar)
for i in range(1,mx+1): #finding the commulative frequency
    fr[i]=fr[i-1]+fr[i]

for i in reversed(range(len(ar))): #now final part, initialization in the corresponding position
    out[fr[ar[i]]-1]=ar[i]
    fr[ar[i]]-=1#updating the commulatinve freq for future use
print(*out) #printing the output