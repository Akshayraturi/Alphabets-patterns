
#T
row=int(input("Enter the number of rows:"))

for i in range(row):
    for j in range(row):
        if j==row//2 or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()