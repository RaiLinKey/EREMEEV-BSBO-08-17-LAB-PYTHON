lenta = [0 for _ in range(30001)]
position = 0
f = False  # флаг открытия скобок
s = False  # флаг закрытия скобок
for cmd in input():
    test = lenta[position]
    if cmd == '[':
        f = True
    elif f and not s and cmd == '-':
        lenta[position] = 1
    elif cmd == ']':
        s = True
    if f and s:
        f = False
        s = False
    elif cmd == '>':
        position += 1
    elif cmd == '<':
        position -= 1
    elif cmd == '+':
        lenta[position] += 1
    elif cmd == '-':
        lenta[position] -= 1
    elif cmd == '.':
        print(lenta[position])
    if lenta[position] > 255:
        lenta[position] = 0
    elif lenta[position] < 0:
        lenta[position] = 255
