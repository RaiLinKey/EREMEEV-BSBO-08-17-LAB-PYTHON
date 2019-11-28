import time
base = ['Иван', 'Андрей', 'Александр', 'Дмитрий', 'Виктория', 'Елизавета', 'Юлия', 'София', 'Мария']


def hello(name):
    print('Здравствуйте,', name, '. Вашу карту ищут...')


def search_card(name):
    if name in base:
        print('Ваша карта с номером', (base.index(name) + 1), 'найдена!')
    else:
        print('Ваша карта не найдена')


print('Работа начата. Пишите имя пациента.')
print('Чтобы остановить работу напишите "СТОП".')
while 1:
    patient = input()
    if patient.lower() in ['стоп', 'stop']:
        break
    else:
        hello(patient)
        time.sleep(5)
        search_card(patient)
