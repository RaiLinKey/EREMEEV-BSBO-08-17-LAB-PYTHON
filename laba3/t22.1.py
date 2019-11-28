alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
       'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
fla = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
       'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encrypt_caesar(msg, shift):
    str1 = ''
    for i in msg:
        if i in alf:
            ind = alf.index(i)
            str1 += alf[ind + shift]
        elif i in fla:
            ind = fla.index(i)
            str1 += fla[ind + shift]
        else:
            str1 += i
    return str1


def decrypt_caesar(msg, shift):
    str1 = ''
    for i in msg:
        if i in alf:
            ind = alf.index(i)
            str1 += alf[ind - shift]
        elif i in fla:
            ind = fla.index(i)
            str1 += fla[ind - shift]
        else:
            str1 += i
    return str1


message = input('Введите сообщение: ')
s = int(input('Смещение: '))
z = encrypt_caesar(message, s)
print(z)
print(decrypt_caesar(z, s))
