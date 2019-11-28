def solve(*coefficients):
    if len(coefficients) == 3:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            return x1, x2
        elif d == 0:
            x1 = (-b) / (2 * a)
            return x1
        elif d < 0:
            return 'NULL'
    elif len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        if b != 0:
            x = -c / b
            return x
        else:
            return 'NULL'
    elif len(coefficients) == 1:
        c = coefficients[0]
        if c == 0:
            return c
        else:
            return 'NULL'
    else:
        return 'None'


print(solve(1, 2, 1))
