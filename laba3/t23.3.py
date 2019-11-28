gl = {'а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я'}

str1 = input('').split(' ')
k = 0
for i in str1:
    for j in i:
        if j in gl:
            k += 1

if k % 2 == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')
