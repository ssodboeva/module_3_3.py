# Функция с параметрами по умолчанию:

def print_params (a = 1, b = 'строка', c = True):
    print  (a, b, c)
print_params ()
print_params (a = 1, b = 'строка')
print_params (a = 1)
# print_params (a = 1, b = 'строка', c= True, d = 'ananas') ошибка, так как функция не содержит агумент "d"
print_params (b = 25) # аргумент 'b' изменен при вызове функции
print_params (c = [1, 2, 3]) # агумент 'c' изменен при вызове функции

#  Распаковка параметров:

values_list = [7, 'home', False]
values_dict = {'a' : 9, 'b' : 'cat', 'c' : True}
print_params (*values_list)
print_params (** values_dict)

# Распаковка + отдельные параметры:

values_list_2 = [11, 'butter']
print_params (*values_list_2, 42)
print_params
