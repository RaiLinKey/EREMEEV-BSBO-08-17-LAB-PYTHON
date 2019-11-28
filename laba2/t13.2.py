n = int(input('Количество чисел: '))
chi = []
for i in range(n):
    chi.append(int(input('Число: ')))
for j in range(0, n-1):
    for i in range(0, n-j-1):
        if chi[i] > chi[i+1]:
            chi[i], chi[i+1] = chi[i+1], chi[i]
for i in chi:
    print(i)
