def month_name(n, lang):
    if lang == 'en':
        if n == 1:
            print('January')
        elif n == 2:
            print('February')
        elif n == 3:
            print('March')
        elif n == 4:
            print('April')
        elif n == 5:
            print('May')
        elif n == 6:
            print('June')
        elif n == 7:
            print('July')
        elif n == 8:
            print('August')
        elif n == 9:
            print('September')
        elif n == 10:
            print('October')
        elif n == 11:
            print('November')
        elif n == 12:
            print('December')
    elif lang == 'ru':
        if n == 1:
            print('Январь')
        elif n == 2:
            print('Фувраль')
        elif n == 3:
            print('Март')
        elif n == 4:
            print('Апрель')
        elif n == 5:
            print('Май')
        elif n == 6:
            print('Июнь')
        elif n == 7:
            print('Июль')
        elif n == 8:
            print('Август')
        elif n == 9:
            print('Сентябрь')
        elif n == 10:
            print('Октябрь')
        elif n == 11:
            print('Ноябрь')
        elif n == 12:
            print('Декабрь')


print('№ месяца:')
number = int(input())
print('Язык [en / ru]:')
language = input()
month_name(number, language)
