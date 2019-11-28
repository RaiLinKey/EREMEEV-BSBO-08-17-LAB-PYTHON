r = input('Порядок выпадения: ')
k = 0
i = 0
m = 0
while i != len(r):
    if r[i] == 'о':
        k = k + 1
    elif (r[i] == 'р' and m < k) or (i == len(r)-1 and m < k):
        m = k
        k = 0
    i = i + 1
print(m)
