old_joke = []


def print_only_new(message):
    if message not in old_joke:
        old_joke.append(message)
        print('SCREEN: ', message)


print('Внимание: шутка!')
while 1:
    text = input()
    if text != '!':
        print_only_new(text)
    else:
        break
