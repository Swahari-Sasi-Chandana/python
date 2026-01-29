#program to print even numbers from 1 to n
i = 0
j= int(input())
while i <= j:
    if i % 2 == 0:
        print(i, end="\t")
    i+=1

