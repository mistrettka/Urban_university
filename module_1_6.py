my_dict = {'Freddie': 1946, 'Brayan':1947, 'John':1951, 'Roger': 1949}

print(my_dict)

print(my_dict['Freddie'])

print(my_dict.get('Mike', 'There is no such person anymore'))


my_dict.update ({'Adam' : 1982,
                 'Kerry' : 1979})
print(my_dict)

print(my_dict.pop('Kerry'))

print(my_dict)


#my_set = {'Queen', 123456, 78.9}
#new_set = {'Queen', 65}

set = {1,2, 'Яблоко', 42.314, 1}
print (set)
set.add(5)
set.update([8])
print(set)
set.remove(2)
print(set)
