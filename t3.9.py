send_tel = input('Введите текст телегарммы: ')
p_tel = len(send_tel) * 40

rub = p_tel // 100
kopeyki = p_tel % 100

print('Стоимость сообщения: ' + str(rub) + ' р. ' + str(kopeyki) + ' коп.')
