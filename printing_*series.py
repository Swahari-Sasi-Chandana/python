for i in range(1,4):
    for j in range(1,4):
        print("*",end="  ")
    print()

'''
    * * * 
    * * * 
    * * * 
'''

for i in range(5):
    for j in range(4):
        print("*",end=" ")
    print()
'''

   * * * *
   * * * *
   * * * *
   * * * *
   * * * *
'''

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="  ")
    print()

'''
    * * *
    * *
    *
'''

n=5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()
'''
    *
   ***
  *****
 *******
*********
'''




for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="  ")
    print()
    '''
       * 
       * *
       * * *



'''

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="  ")
    print()
'''
        * * * *
        * * *
        * *
        *

'''

  

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="  ")
    print()

'''
   1
   1 2
   1 2 3
'''    
   

 
 

for i in range(1,4):
    for j in range(1,i+1):
        print(i,end="  ")
    print()
'''
  1
  2 2
  3 3 3
'''
