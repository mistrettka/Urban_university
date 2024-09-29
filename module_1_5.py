immutable_var = (1, 2, 'a', 'b')

print(immutable_var)

print(type(immutable_var))

#immutable_var[0] = 9

#Мы не можем изменить кортеж, в этом его основные преимущества. Он относитяс к неизменяемым типам данных,
# эдакая "коллекция определенных знаков". Кортеж необходим для создания одноразовых программ, которые
# не должны занимать много места. Кортеж хранит ссылку на список, а не сам список,
# если обратиться к кортежу по индексу и заменить в нём какой-то элемент - это вызовет ошибку.

mutable_list = [1, 2, 'a', 'b', 'Modified']

mutable_list [0] = 10
mutable_list [1] = 11
mutable_list [2] = 'c'
mutable_list [3] = 'v'
mutable_list[4] = 'modify'

print(mutable_list)