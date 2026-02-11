#Conversion of Binary number to Decimal Number
a=int(input())
d=0
i=0
while (a!=0):
    r=a%10
    d=d+r*(2**i)
    a=a/10
    i+=1
print(d)
