k = int(input('Количество наименований: '))
pok = []
kol_vo = []
for i in range(k):
    pok.append(input('Наименование покупки: '))
    kol_vo.append(input('Количество: '))
for j in range(k - 1, -1, -1):
    print(pok[j], kol_vo[j])
