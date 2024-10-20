#WAP TO PRINT THE BORDER ELEMENTS OF A 4X4 2D ARRAY

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]

for i in range(4):
    for k in range(4):
        if(i == 0 or i == 3 or k == 0 or k == 3):
            print(arr[i][k], end=" ")
        else:
            print(" ", end=" ")
    print()