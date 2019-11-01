print('Добро пожаловать в лучший тест личности!')
print('Пишите номер ответа.')
rez = 0
scope = [1, 2, 3, 4]
f = 1
while True:
    q1 = int(input('\nВы любите животных?\n1) Очень\n2) Ну да\n3) Нет\n4) Ненавижу\n\nВаш ответ: '))
    if q1 in scope:
        rez += q1
    else:
        print('\nВведено неверное значение.')
        f = 0
        break

    q2 = int(input('\nВы добрый человек\n1) Очень\n2) Ну да\n3) Нет\n4) Абсолютно нет\n\nВаш ответ: '))
    if q2 in scope:
        rez += q2
        break
    else:
        print('\nВведено неверное значение.')
        f = 0
        break
if f == 1:
    print('')
    if (rez < 3) and (rez > 0):
        print('Ты солнышко :)')
    elif rez == 3:
        print('Ты весьма неплохой человек')
    elif rez == 4:
        print('А ты хорош(а)')
    elif rez == 5:
        print('С тобой чтоит быть осторожней')
    elif rez == 6:
        print('Тебя вообще воспитывали?')
    elif rez > 6:
        print('Фу таким быть')
    else:
        print('Что-то пошло не так •_•')
