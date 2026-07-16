import os 

if os.path.exists('dummmy.txt'):
    print('File exists')
else:
    print('File does not exist')

content = ''

with open('class_notes.txt','r') as f1:
    content += 'This is the First File\n'
    content += '*'*25
    content += '\n' +f1.read() + '\n'

with open('something.txt','r') as f2:
    content += 'This is the Second File\n'
    content += '*'*25
    content += '\n' +f2.read() + '\n'

with open('dummy.txt', 'w') as out:
    out.write(content)
print('Saved all data to dummy.txt')