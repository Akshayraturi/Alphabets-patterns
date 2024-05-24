
#V
row=int(input("Enter the number of rows:"))

if (row%2==0):
    row-=1
else:
    row=row
for i in range(row):
    for j in range(row):
        if (i==j and j<=row//2) or (i+j==row-1 and j>row//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
