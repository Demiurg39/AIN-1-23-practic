# TODO Условные операторы, и циклы

# # TODO if-если, elif-другое если, else-если все прочие проверки не прошли = условные операторы
# color = str(input('Color of the traffic lighter')).lower()

# if color == 'red':
#     print(f'Now is {color} STOP!')
# elif color == 'yellow':
#     print(f'Now is {color} Wait...')
# elif color == "green":
#     print(f"Now is {color} Let's go!")
# else:
#     print(f"Something isn't right... \"{color}\" is that right?")

# ==. >=. <=. !=, or, and, not условные операнды

# # TODO taurus from 21 of april to 20 of may(проверка )

# day = int(input('Day of your birth?: ')) # День рождения
# mounth = int(input('Mounth of your birth?(by numbers): ')) # Месяц цифрой
# if (day >= 21 and day <= 30 and mounth == 4) \
#                         or (day >= 1 and day <= 20 and mounth == 5):
#     print('You are Taurus')
# else:
#     print('You are not Taurus')

# # TODO цикл for работает как отрезок
# # TODO цикл while работает до тех пор пока условие правдиво

# apples = 10
# good = 0
# bad = 0

# while apples != 0:
#     answer = str(input('Is that apple good?\n(good)(bad): ')).lower()
#     if answer == 'good':
#         good += 1
    
#     elif answer == 'bad':
#         bad += 1

#     apples -= 1

# print(f'Всего яблок:{apples}\nХороших: {good}\nПлохих: {bad}')

# # TODO break, continue
# color = str(input('Color of the traffic lighter')).lower()

# while True:
#     if color == 'red':
#         print(f'Now is {color} STOP!')

#     elif color == 'yellow':
#         print(f'Now is {color} Wait...')

#     elif color == "green":
#         print(f"Now is {color} Let's go!")

#     else:
#         print(f"Something isn't right... \"{color}\" is that right?")
    
#     answer = str(input('Do you want to quit?\n(yes)(no): ')).lower()
#     if answer == 'yes':
#         continue

#     elif answer == 'no':
#         print('Auf wiedersehen:)')
#         break

# while True:
#     name = str(input('Input your name: '))
#     age = int(input('Input your age: '))

#     if age < 18:
#         print('Sorry, you are not allowed to answer:(')
    
#     elif age >= 18 and age <= 40:
#         city = str(input('Input where are you from: ')).lower()

#         if city == 'бишкек' or city == 'bishkek': 
#             money_amount = int(input('What is your money amount?: '))
            
#             if money_amount >= 100:
#                 print('Welcum:)')
#                 break
#             else:
#                 print('You are NOT allowed here\nGET LOST!!1!')
#                 break
#         else:
#             print('Welcome to Bishkek!')
    
#     else:
#         print("Isn't you are too old?")