men = int(input('Введите количество имён: '))
men_works = [input('Введите имя: ') for _ in range(men)]
result = 0
for example in set(men_works):
    c = 0
    for name in men_works:
        if example == name:
            c += 1
    if c > 1:
        result += c
print(result)
