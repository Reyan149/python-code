import os 

if os.path.exists('dummmy.txt'):
    os.remove('dummmy.txt')
    print('dummmy.txt file deleted')

else:
    print('File does not exist')