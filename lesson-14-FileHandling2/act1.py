content = open("class_notes.txt","r")
lines = content.readlines()
print(lines)
print(f"The return type of readlines(): {type(lines).__name__}")

content.seek(0)

print("\nFirst 20 characters of the file:")
print("*" * 20)
print(content.read(20))
print("*" * 20)

for line in lines:
    print(line)