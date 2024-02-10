import matplotlib.pyplot as plt
import matplotlib

row=int(input("Enter the number of rows:"))
col=row+2
for i in range(row):
    for j in range(col):
        if i==0 or i==(row-1) or j==0 or j==(col-1):
            print("--",end=" ")
        else:
                print("--",end=" ")
                print()


