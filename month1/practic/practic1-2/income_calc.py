#! Python3
# Программа которая подсчитывает средний доход

# Данные за первый месяц
month1_income = float(input('mounth-1\nEnter Your income for mounth > '))
month1_rent = float(input('Enter rental price for mounth > '))
month1_food = float(input('Enter food price for mounth > '))
month1_transport = float(input('Enter transportion price for mounth > '))
month1_entertaiment = float(input('Enter entertaiment price for mounth > '))

# Данные за второй месяц
month2_income = float(input('mounth-2\nEnter Your income for mounth > '))
month2_rent = float(input('Enter rental price for mounth > '))
month2_food = float(input('Enter food price for mounth > '))
month2_transport = float(input('Enter transportion price for mounth > '))
month2_entertaiment = float(input('Enter entertaiment price for mounth > '))

# Высчет средних значение
mid_income = (month1_income+month2_income)/2 # Средняя зарплата за n месяцев
mid_spend = ((month1_food+month1_entertaiment+month1_rent+month1_transport)+\
            (month2_food+month2_entertaiment+month2_rent+month2_transport))/2 # Средний расход за n месяцев
mid_clear_income = mid_income-mid_spend # Чистый доход за n месяцев

# Вывод значений
print(f'Средний доход: {round(mid_income, 2)}')
print(f'Средний расход: {round(mid_spend, 2)}')
print(f'Чистый доход: {round(mid_clear_income, 2)}')
