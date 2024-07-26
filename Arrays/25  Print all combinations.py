def tree(i,j):
    if i == r: # if the combination is reach to r element, print the combination
        for k in range(r):
            print(comb[k], end="")
        print()
        return # dismiss the recursion after printing
    
    if j>=n: # if j is reach to the size of the list
        return
    
    comb[i]=ar[j]
    tree(i+1,j+1) # if we include the current element to the tree

    while j<n-1 and ar[j]==ar[j+1]: #handling (skip) the duplicates
        j+=1
    
    tree(i,j+1) # if we not include the current element to the combination



if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    r = 3
    n = len(ar)
    ar.sort()
    comb=[0]*r 
    tree(0,0)