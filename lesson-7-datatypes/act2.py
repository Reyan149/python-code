myDict = {}

my_dict = {
    1 : "APPLE",
    2 : "BANANA",
}

my_dict2 = {
    "name" : "John",
    "age" : 30,
    101 : [1,2,3]
}

print(myDict)
print(my_dict[1])
print(my_dict2['name'])

my_dict2['age'] = 20
print(my_dict2['age'])

my_dict2['address'] = 'Downtown, LA'
print(my_dict2)

print('Address : ', my_dict2.get('address'))


my_dict2.clear()
print(my_dict2)