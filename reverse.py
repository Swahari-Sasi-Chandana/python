#reverse
n=int(input())                                  #number of elements
l=list(map(int,input().split()))                #input list
s,e=map(int,input().split())                    #start and end index
bs=l[0:s]                                       #elements before start index
afs=l[e+1:n]                                    #elements after end index
sr=l[s:e+1]                                     #sublist to be reversed
sr.sort(reverse=True)                           #reverse the sublist
res=bs+sr+afs                 #final list after merging
for i in res:
    print(i,end=' ')
