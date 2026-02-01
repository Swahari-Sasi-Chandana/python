# Factorial in diffrent ways in functions
def factorial(n):
    if num < 0:
        print("Factorial is not defined for negative numbers")
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))
print(factorial(num))



def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Factorial:",fact)

#in For loop 
a=int(input())
if a==0 or a==1:
    print("1")
elif a<0:
    print("Factorial is not defined for negative numbers")
else:
    factorial(a)

#in While Loop
def factorial(n):
    fact=1
    i=1
    while i<=n:
        
        fact*=i
        i+=1
    print("Factorial:",fact)


a=int(input())
if a==0 or a==1:
    print("1")
elif a<0:
    print("Factorial is not defined for negative numbers")
else:
    factorial(a)
