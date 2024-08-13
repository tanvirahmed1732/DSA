#https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
m = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16], 
     [17, 18, 19, 20]] 
c=4
r=5
for i in range(1,c+r):
    #from where to print
    if i<=r:
        start=0
    else:
        start=i-r

    #how many element to print
    count=min(i,c-start)
    for j in range(count):
        print(m[min(r,i)-j-1][start-j],end=" ")
    print()

