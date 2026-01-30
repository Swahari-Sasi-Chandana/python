#Swap to seperate even numbers one side and odd numbers another side

n=int(input())
a=list(map(int,input().split()))
ev=[]
odd=[]
for i in a:
    if i%2==0:
        ev.append(i)
    else:
        odd.append(i)
ev.extend(odd)
for i in ev:
    print(i,end=' ')
