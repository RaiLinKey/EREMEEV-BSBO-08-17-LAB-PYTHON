lst = []

while True:
    word = input()
    if word == '':
        break
    lst.append(word)

print(*sorted(lst, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')
