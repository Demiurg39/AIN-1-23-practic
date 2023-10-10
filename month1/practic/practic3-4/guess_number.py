toss = int(input('Enter number in range (0, 100), and computer will guess it\n> '))
tries = 0
lower = 1
highest = 100

while True:
    guess = (lower+highest)//2
    print(f'Computer said: {guess}')
    if guess == toss:
        break 
    
    elif guess > toss:
        highest = guess-1
    
    else:
        lower = guess+1

    tries += 1    
    print(f'Attemp: {tries}')

print(f'\nComputer find: {guess}')