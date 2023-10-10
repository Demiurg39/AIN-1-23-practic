# Константы для гласных и согласных
VOWEL = 'ауоыэяюёиеaeiou'
CONSONANTS = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz'

# Бесконечный цикл
while True:
    word = str(input('Enter a word to count \n> '))
    vowel_count = 0
    const_count = 0

    # Цикл для подсчета гласных/согласных
    for letter in word.lower():
        if letter in VOWEL:
            vowel_count += 1

        elif letter in CONSONANTS:
            const_count += 1

    print(f'--- Всего символов {len(word)}\n\
--- Всего гласных {vowel_count}\n\
--- Всего согласных {const_count}\n\
--- Процентное соотношение {round((vowel_count/len(word)*100), 2)}/{round((const_count/len(word)*100), 2)}')       

    # По желанию выход из цикла    
    answer = str(input('Do you want to continue?(y/n) \n> ')).lower()
    if answer.startswith('n'):
        break
