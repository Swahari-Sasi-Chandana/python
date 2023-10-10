p=int(input("Enter Principal amount"))
t=int(input("Enter Time"))
r=int(input("Enter Rate of Interest"))
si=p*t*r/100
print("SI:",si)
emi=si+p/12*t
print ("EMI is :",emi)
