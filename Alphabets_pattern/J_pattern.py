
#J
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if j==row//2 or i==0 or (i==row-1 and j<=row//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()