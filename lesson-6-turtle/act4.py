print('Type stop to end the program')
list = []
while True:
    hobby = input('What are your favourite hobbies? ')
    if hobby == 'stop':
        break
    list.append(hobby)
print('Your hobbies are: ' + ', '.join(list))