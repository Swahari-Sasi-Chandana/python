i=1
num = int(input('Enter a number'))
flag=0

while i < num:
    if(num % i) == 0:
        flag = flag +1
    i = i+1

if flag==1:
    print('Number is a Prime Number')
else:
    print('Number  is not a Prime Number')
