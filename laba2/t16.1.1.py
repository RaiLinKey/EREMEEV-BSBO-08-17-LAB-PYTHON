def block(l_code):
    opened = []
    blocks = {}
    for i in range(len(code)):
        if code[i] == '[':
            opened.append(i)
        elif code[i] == ']':
            blocks[i] = opened[-1]
            blocks[opened.pop()] = i
    return blocks


def parse(l_code):
    return ''.join(c for c in l_code if c in '><+-.,[]')


def run(l_code):
    l_code = parse(l_code)
    x = i = 0
    bf = {0: 0}
    blocks = block(l_code)
    l = len(l_code)
    while i < l:
        sym = l_code[i]
        if sym == '>':
            x += 1
            bf.setdefault(x, 0)
        elif sym == '<':
            x -= 1
        elif sym == '+':
            bf[x] += 1
        elif sym == '-':
            bf[x] -= 1
        elif sym == '.':
            print(chr(bf[x]), end='')
        elif sym == ',':
            bf[x] = int(input('Input: '))
        elif sym == '[':
            if not bf[x]:
                i = blocks[i]
        elif sym == ']':
            if bf[x]:
                i = blocks[i]
        i += 1


code = input()
run(code)
