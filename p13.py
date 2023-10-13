year=int(input("Enter year:"))
if year%4==0 and year%100!=0:
  print("Leap year",year)
elif year%400==0:
  print("Leap year",year)
else:
  print("Not a leap year",year)
