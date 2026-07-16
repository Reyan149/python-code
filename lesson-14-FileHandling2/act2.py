word = input("Enter lines starting with:")

file = open("class_notes.txt", "r")
lines = file.readlines()

for line in lines:
     if line.startswith(word):
        continue
     else:
        print(line)
file.close()