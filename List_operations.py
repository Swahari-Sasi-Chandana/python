#List Operations
a=int(input("Enter the Limit of List for Operations:"))
b=list(map(int,input("Enter numbers upto limit:").split()))
if len(b) != a:
    print("Incorrect limit")
    b=list(map(int,input("Enter numbers upto limit:").split()))
    print("Given List  :", b)
else:
    print("Given List  :", b)
b.append(int(input("Enter a number to Append in List:")))
print("List after appending an element:", b)
b.remove(int(input("Enter a number in above List to remove")))
print("List after removing an element:", b)
b.sort()
print("List after sorting:", b)
b.reverse()
print("List after reversing  elements:", b)
