n = input('Введите букву: ')
str1 = input('Введите строку: ').split(' ')
for i in str1:
    if n in i.lower():
        print(i)
