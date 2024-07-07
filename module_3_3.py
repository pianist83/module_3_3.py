def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params("Pianist")
print_params("Piamist", False, 1965)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ["Pianist", 1983, True]
values_dict = {'a':1, 'b':'строка', 'c':True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Pianist", 1983]
print_params(*values_list_2, 42)