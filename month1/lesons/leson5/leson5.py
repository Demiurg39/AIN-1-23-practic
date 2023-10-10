# Функции, лямбда(анонимные) функции


# # try: except:

while True:
    try:
        num1 = float(input('number\n> '))
        operator = input('operator(+-/*)\n> ')
        num2 = float(input('number\n> '))
    except TypeError:
        print('ONLY DIGITS!!!')
        continue

    if operator == '+':
        print(num1+num2)
    elif operator == '-':
        print(num1-num2)
    elif operator == '/':
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print('YOU CANNOT DIVIDE BY ZERO!!!')
    elif operator == '*':
        print(num1*num2)
# try:
#     num1 = 22
#     num2 = '22'
#     print(num1+num2)
# except:
#     print('smth got wrong')

# # lambda def 

# plus = lambda x, y: x+y
# print(plus(1,3))
     
# # # # #
# army = []
# kollege = []
# married = []
# university = []

# abiturients = [
#     {'name' : 'Nikita', 'ORT' : 110, 'gender' : 'male'},
#     {'name' : 'Andrey', 'ORT' : 220, 'gender' : 'male'},
#     {'name' : 'Asya', 'ORT' : 70, 'gender' : 'female'},
#     {'name' : 'Maria', 'ORT' : 87 , 'gender' : 'female'},
#     {'name' : 'Asan', 'ORT' : 30, 'gender' : 'male'},
#     {'name' : 'Karina', 'ORT' : 10, 'gender' : 'female'},
#     {'name' : 'Mark', 'ORT' : 30, 'gender' : 'male'},
#                ]

# def all_abit(list_:list):
#     for i in list_:
#         for key, value in i.items():
#            print(f'{key}-{value}')
# # all_abit(abiturients)
# # FIXME
# def selection(abiturients:list, army:list, kollege:list, married:list, university:list):
#     for person in abiturients:
#         if person['ORT'] >= 110:
#             university.append(person)
#         elif person['ORT'] < 110:
#             kollege.append(person)
#         elif person['ORT'] < 80 and person['gender'] == 'male':
#             army.append(person)
#         elif person['ORT'] < 80 and person['gender'] == 'female':
#             married.append(person)
# # FIXME
# selection(abiturients, army, kollege, married, university)
# print(university)
# print(kollege)
# print(army)
# print(married)

# # Множественное значение аргументов
# def menu(**kwargs):
#     return kwargs

# print(menu(breakfast='eggs', dinner='meat'))


# def plus_number(*args):
#     return sum(args)/len(args)

# print(plus_number(1,223,5.2,34,2,1235,6,2,123,123,0.2,))

# count = 4
# while count > 0:
#     numbers = int(input('numbers:'))
#     count -= 1

# def plus(num1, num2=12):
#     # return num2+num1

# print(plus(1))

# def about_my_self(name, age, hobby, pets):
#     return (f'Меня зовут {name}\n'
#             f'Мне {age} лет\n'
#             f'Мое хобби {hobby}\n'
#             f'У меня живет {pets}')

# print(about_my_self('Amir', 1007, 'icpc', None))

# def summa(num1, num2, num3, num4):
#     return (num1+num2+num3+num4)

# print(summa(1,2,3,4))

# def summa(num1, num2):
#     print(num1+num2)

# summa(1,2)

# def greeting(name):
#     print(f'Привет {name}')

# count = 4
# while count != 0:
#     count -= 1
#     greeting(input('Как вас зовут?\n> '))
