
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(7, 55)
print_params(c = False)
# print_params(4, 5, 6, 7) #ошибка из-за несовпадения количества аргументов и параметров
print_params(b = 25)
print_params(c = [1,7,55.68])

values_list = ['str', [1, 77, 99.99], True]
values_dict = {'a': 55.3, 'b': False, 'c': '3'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [{1, 2}, 'string']
print_params(*values_list_2, 42) # работает, поскольку параметры заполнились за счет распаковки списка
