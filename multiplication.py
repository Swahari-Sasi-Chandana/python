for i in range(0,6):
    for j in range(0,6):
        print(i*j,end="  ")
    print()

for i in range(0,6):
    for j in range(0,6):
        if i==0:
            if j==0:
                print("*",end=" ")
            else:
                print(j, end=" ")
        else:
            if j==0:
                print(i,end=" ")
            else:
                print(i*j,end=" ")
    print()


'''
        * 1 2 3 4
        1 1 2 3 4
        2 2 4 6 8
        3 3 6 9 12
        4 4 8 12 16
'''
