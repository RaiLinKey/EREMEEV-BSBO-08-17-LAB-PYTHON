def translate(text):
    vowels = ['У', 'у', 'Е', 'е', 'Ё', 'ё', 'Ы', 'ы', 'А', 'а',
              'О', 'о', 'Э', 'э', 'Я', 'я', 'И', 'и', 'Ю', 'ю']
    piece_text = []
    for i in text:
        if i not in vowels:
            piece_text.append(i)
    return ''.join(piece_text)


print('Введите текст на русском языке:')
str1 = input()
print(translate(str1))
