def same_by(ch, ob):
    for i in range(len(ob) - 1):
        if ch(ob[i]) != ch(ob[i + 1]):
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')