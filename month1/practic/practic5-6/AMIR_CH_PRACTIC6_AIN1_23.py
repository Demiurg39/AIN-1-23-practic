data_tuple = ('G', 6.13, 'I', 'b', 'n', True, 'o', 't', 3, 'Y', 1, 'p')

letters = []
numbers = []

for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
bool_ = numbers.pop(0)
letters.append(bool_)
numbers.insert(1, 2)
numbers = [i**3 for i in numbers]
numbers = sorted(numbers)
numbers = tuple(numbers)
bool_ = letters.pop(-1)
letters = sorted(letters, reverse=True)
letters.append(bool_)

# for i in letters:
#     if isinstance(i, str):
#         if i.lower() == 'p' or i.lower() == 'b':
#             letters_.append(i.upper())
#         letters_.append(i)

print(numbers)
print(letters)