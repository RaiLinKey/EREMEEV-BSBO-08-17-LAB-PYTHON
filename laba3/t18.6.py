def line(s, t):
    k = float(s[:s.index('x')])
    b = float(s[s.index('x') + 1:])
    x = float(t[:t.index(';')])
    y = float(t[t.index(';') + 1:])
    print((k * x + b) == y)
    y0 = k * x + b
    return y0 == y


print('Введите уравнение прямой [в виде kx + b]:')
s1 = input()
print('Введите координаты точки [в виде x;y]:')
t1 = input()
line(s1, t1)
