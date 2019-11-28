def palindrome(s):
    s = s.replace(' ', '').lower()
    s_1 = s[::-1]
    if s_1 == s:
        print('Палиндром')
    else:
        print('Не палиндром')


print('Введите строку:')
text = input()
palindrome(text)
