#N
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if j==0 or i==j or j==row-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()