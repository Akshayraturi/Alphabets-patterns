
#W
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if (j==i and i>=row//2) or(i+j==row-1 and i>row//2) or j==0 or j==row-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()