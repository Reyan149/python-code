with open('something.txt','r') as f1:
    for line in f1:
        words = line.split()
        print(f'{line} : {len(words)}')