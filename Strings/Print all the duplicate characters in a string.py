s=input()
c={} #this is a dictionary
for i in s:
    if i in c:
        c[i]+=1 # if the item is already exist in the dict.
    else:
        c[i]=1 # new assigning the item in the dictionary, in the index of i.
for i,j in c.items(): 
    if j>1: # print all tiem in the dictionary which has the value of greater than 1.
        print(i," count = ",j)