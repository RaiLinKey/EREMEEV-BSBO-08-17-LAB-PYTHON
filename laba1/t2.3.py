answer = input('— Привет! Как у тебя дела?\n— ')
good_answer = ['хорошо', 'норм', 'нормально', 'неплохо', 'отлично', 'прекрасно']
bad_answer = ['плохо', 'не очень', 'ужасно', 'отвратительно']
if answer.lower() in good_answer:
    print('— Отлично, у меня тоже всё хорошо :)')
elif answer.lower() in bad_answer:
    print('— Не расстраивайся, жизнь прекрасна и удивительна!')
else:
    print('— Я тебя не понимаю :(')
