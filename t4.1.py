print('Вы можете выговориться. Чтобы остановиться напишите "Спасибо."\n')
count = 0
while True:
    a = input()
    if a.lower() in ['спасибо.', 'спасибо']:
        break
    count += 1
print('\nКоличество высказываний: ' + str(count))
