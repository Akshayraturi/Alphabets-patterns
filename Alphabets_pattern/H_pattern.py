#H
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if j==0 or j==row-1 or i==row//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
