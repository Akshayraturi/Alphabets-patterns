

#U
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if (j==0 and i!=row-1) or (i==row-1 and j!=0 and j!=row-1) or(j==row-1 and i!=row-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()