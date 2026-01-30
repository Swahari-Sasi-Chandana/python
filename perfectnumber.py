#program to print given number is perfect or not
def perfect(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum=sum+i
    if a==sum:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


t=int(input("Enter number of test cases"))
for i in range(1,t+1):
    a=int(input())
    perfect(a)
