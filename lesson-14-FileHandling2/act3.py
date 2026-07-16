content = open("class_notes.txt", "r")
lined = content.readlines()
content.close()

outFile = open("odd_lines.txt", "w")

for i in range(0, len(lined),2):
    outFile.write(lined[i])

outFile.close()
print("odd lines are saved to the file")