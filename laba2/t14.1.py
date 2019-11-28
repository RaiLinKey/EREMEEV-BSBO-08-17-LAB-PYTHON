n = int(input('Количество пунктов: '))
rez = []
for i in range(n):
    a = input()
    if 'лук' not in a:
        rez.append(a)
print(', '.join(rez))
