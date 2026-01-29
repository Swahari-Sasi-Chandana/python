m=[]
s=0
n=int(input())
for i in range(n):
    x=int(input("Enter number:"))
    m.append(x)
for i in range(1, n):
    if m[i]< m[i-1]:
        min=m[i]
print(m[i])
