my_dict = {'Den': 1999, 'Mike': 2002, 'Kat': 2005}
print('Dict:', my_dict)

print('Existing value:', my_dict.get('Den'))
print('Not existing value:', my_dict.get('Tad'))
my_dict.update({'Nik': 1998, 'Fred': 1990})
print('Modified dictionary:', my_dict)
print('Deleted value:', my_dict.pop('Mike'))

my_set = {1, 'Nike', 1, 3, 'Nike', (1, 2)}
print('Set:', my_set)
my_set.update({334, 777})
print('Modified set: ', my_set)
my_set.remove(334)
print(my_set)