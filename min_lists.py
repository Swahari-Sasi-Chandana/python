#program to find minimum from two lists
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.extend(b)
print(min(a))
