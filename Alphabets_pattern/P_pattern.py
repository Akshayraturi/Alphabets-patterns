
# P

row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if  (i==0 and j!=row-1) or (j==0 and i!=0 ) or j==0 or (i==row//2 and j!=row-1) or(j==row-1 and i<row//2 and i!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()