myfile = open('testFile.txt','w')

myfile.write('Hello I am Reyan\n')
myfile.write('I live in the UK\n')
myfile.write('I go to school\n')
myfile.close()

item_list_path = 'item-list.txt'

myfile2 = open(item_list_path, "r")
content = myfile2.read()
print(content)
myfile2.close()