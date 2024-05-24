
# C pattern
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if (i==0 and j!=0) or (j==0  and i!=0 and i!=row-1) or (i==row-1 and j!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
