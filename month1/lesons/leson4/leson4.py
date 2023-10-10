# # Структуры данных
# # Списки кортежи словари

# # Списки(list) - []
# name = 'Smith'
# name = list(name)
# print(name)

# numbers = [1,2,3,4,22,3334,21,2,43]
# print(numbers.sort())
# print(numbers)

# lang = 'python'
# lang = list(lang)
# print(lang.reverse())

# # Перемещение элементов с одного списка в другой
# men = ['Kirill', 'Anthon', 'Ivan', 'Asan']
# women = ['Masha', 'Vera', 'Eliza', 'Aida']
# women.insert(1, men.pop(0))
# print(women)

# person = []
# person.extend(men)
# person.extend(women)
# print(person)

# data_type = [True, False, 'Edication', 123, 32.43]
# string = []
# numbers = []
# bool_ = []

# for i in data_type:
#     if isinstance(i, str):
#         string.append(i)
#     elif isinstance(i, bool):
#         bool_.append(i)
#     else:
#         numbers.append(i)

# print(string)
# print(numbers)
# print(bool_)


# data_types = ['hello', 12, 12, True, 'string', False, 32.44, 12]
# # Добавление значения
# # Изменение значения
# # Удалять значения

# data_types.append('INAI')
# data_types.append('DJAL')
# data_types.insert(1, 'qwerty')
# data_types.append(name)

# data_types[0] = 'world'

# del(data_types[-1])
# data_types.remove(False)

# print(data_types.count(12))
# print(data_types.index(True))

# print(data_types)

# # Кортежи
# nominal = (1,3,5,10,20,50,100,200,500,'1k', '2k', '5k')
# nominal = list(nominal)
# nominal.append('Деньги')
# nominal = tuple(nominal)
# print(nominal)

# # Словари
# student = {
#     'name' : 'Amir',
#     'age' : 17,
#     'height' : 186,
#     'Education' : True,
#     2006 : "date of birth",
#     2007 : True,
#     'numbers' : ['0555293192', '213144141']
# }

# for key, value in student.items():
#     print(f'{key}:{value}')

# # Добавление по ключю
# student['age'] += 1
# # Удаление элемента
# del(student[2007])
# print(student)

# money = [1,3,5,10,20,50,100,200,500,'1k', '2k', '5k']
# persons = ['no', 'no', 'no', 'no', 'Тоголоко Молдо', 'Курмажан Датка', 'Токтогул Сатылганов', 'Алыкул Осмонов',
#            'Саякбай Каралаев', 'Жусуп Баласагын', 'Arnament', 'Чокморов']

# banknotes = dict(zip(money, persons))
# for key, value in banknotes.items():
#     print(f'{key}:{value}')

my_car = dict(model='lexus570', number='09kg009vip', color='black')
my_car.update(model='Volkswagen ID4')
my_car.update(volume='1.4')
print(my_car)
for key, value in my_car.items():
    print(f'{key}:{value}')