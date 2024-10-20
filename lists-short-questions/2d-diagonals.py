#WAP TO PRINT THE DIAGONALS OF A 4X4 2D ARRAY

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]

for i in range(4):
    for k in range(4):
        if(i == k or (i*10+k)%3 == 0):
            print(arr[i][k], end=" ")
        else:
            print(" ", end=" ")
    print()