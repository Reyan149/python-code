def romanToInt(romanInput):
    romanNumerals = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

    resultInteger = 0

    for i in range(0, len(romanInput) - 1 ):
        if romanNumerals[romanInput[i]] < romanNumerals[romanInput[i + 1]]:
            resultInteger -= romanNumerals[romanInput[i]]
        else:
            resultInteger += romanNumerals[romanInput[i]]

# Add the last numeral since it's always added
    resultInteger += romanNumerals[romanInput[-1]]

    return resultInteger

roman = input('Input a Roman numeral :')

print('Integer equivalent : ',romanToInt(roman))