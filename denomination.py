#program to print currency denominations

x=int(input("Enter amount"))
ttn=0
fhn=0
thn=0
hn=0
fn=0
tn=0
ten=0
five=0
two=0
one=0

while x>=2000: 
    ttn+=1
    x=x-2000

while x>=500:
    fhn+=1
    x=x-500
    
while x>=200:
    thn+=1
    x=x-200
    
while x>=100:
    hn+=1
    x=x-100

while x>=50:
    fn+=1
    x=x-50

while x>=20:
    tn+=1
    x=x-20

while x>=10:
    ten+=1
    x=x-10

while x>=5:
    five+=1
    x=x-5

while x>=2:
    two+=1
    x=x-2

while x>=1:
    one+=1
    x=x-1

if ttn>0:
    print("2000:"+str(ttn))
if fhn>0:
    print("500:"+str(fhn))
if thn>0:
    print("200:"+str(thn))
if hn>0:
    print("100:"+str(hn))
if fn>0:
    print("50:"+str(fn))
if tn>0:
    print("20:"+str(tn))
if ten>0:
    print("10:"+str(ten))
if five>0:
    print("5:"+str(five))
if two>0:
    print("2:"+str(two))
if one>0:
    print("1:"+str(one))
