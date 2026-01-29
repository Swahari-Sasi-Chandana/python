#program to identify the file format
file=input()
if file.endswith(".jpeg"):
    print("Photo document")                 #also string function
elif file.endswith(".doc"):                   #sasi.doc
    print("Word document")
elif file.endswith(".xls"):
    print("Excel document")
elif file.endswith(".ppt"):
    print("Powerpoint document")
else:
    print("Invalid document")
