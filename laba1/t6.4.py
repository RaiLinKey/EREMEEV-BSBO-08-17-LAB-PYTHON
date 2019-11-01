kch = int(input('Введите количество человек: '))
total = 0
for i in range(1, kch + 1):
    iq = int(input('Введите IQ: '))
    total += iq
    avr = int(total / i)
    if iq == avr:
        print('0\n')
    elif iq < avr:
        print('<\n')
    elif iq > avr:
        print('>\n')
