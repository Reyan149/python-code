numbersLargest = int(input('Enter Largest number : '))
numberSmallest = int(input('Enter Smallest number'))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numbersLargest % numberSmallest
    numbersLargest = numberStore

print('HCF : ', numbersLargest)