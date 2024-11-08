def print_params(a=1, b='str', c= True):
    print(a, b, c)
values_list = [2, 5.5, 'peach']
values_dict = {'a':4.4, 'b':5, 'c':"egg"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, 'milk']
print_params(*values_list_2, 42)