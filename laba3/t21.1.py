def from_string_to_list(string, container):
    return container + list(map(int, string.split()))


container1 = []
k = int(input('Количество элементов списка: '))
print('Заполните список:')
for i in range(k):
    container1.append(input())
str1 = input('Введите строку:')
print(from_string_to_list(str1, container1))
