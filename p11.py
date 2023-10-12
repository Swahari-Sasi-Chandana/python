s_no=int(input("Enter the student no:"))
s_name=input("Enter the student name:")
group=input("Enter the group:")
s1=int(input("Enter the marks of maths:"))
s2=int(input("Enter the marks of Physics:"))
s3=int(input("Enter the marks of Chemistry:"))
total= s1+s2+s3
avg=total% 3
if(avg>=90):
    print("O-Grade")
elif(avg>=80):
    print("A-Grade")
elif(avg>=70):
    print("B-Grade")
elif(avg>=60):
    print("C-Grade")
elif(avg>=50):
    print("D-Grade")
else:
    print("Pass")


