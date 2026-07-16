# Creating or opening file
myfile = open("testFile.txt","w")

# Writing 
myfile.write("Hello I am Reyan")
myfile.write("\nI live in UK")
myfile.write("\nI go to School")

# Closing the file
myfile.close()

# Read from a file
# Read full content

myfile2 = open("item-list.txt", "r")
content = myfile2.read()
print(content)
myfile2.close()

myfile3 = open("item-list.txt", "a")
myfile3.write("\n5.Washing clothes")
myfile3.write("\n6.Driving")
myfile3.close()

myfile4 = open("item-list.txt", "r")
lines = myfile4.readlines()
print(f"you have {len(lines)} lines in the file")
myfile4.close()
