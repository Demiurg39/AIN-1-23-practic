# Амир Чирягов 5 практика группа  AIN-1-23
countries = {
    'kg': {'red', 'yellow'},
    'ru': {'white', 'red', 'blue'},
    'us': {'blue', 'red', 'white'},
    'tr': {'red', 'white'},
    'it': {'green', 'white', 'red'},
    'uk': {'blue', 'yellow'},
    'abh':{'green','red','white'}
}

while True:
    output = [] 
    colors = input('input colors\n> ')
    colors = colors.split()
    for key, value in countries.items():
        if all([(color in value) for color in colors]):
            print(key)
        else:
            continue
    response = input('do you want to continue?(y/n)\n> ')
    if response.startswith('n'):
        break