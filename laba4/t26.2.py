from PIL import Image, ImageDraw


def board(num, size):
    side = num * size
    new_image = Image.new('RGB', (side, side), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    f = True
    for i in range(0, side, size):
        if f:
            for j in range(size, side, size * 2):
                draw.rectangle((j, i, j + size - 1, i + size - 1), fill=(255, 255, 255), width=size)
        else:
            for j in range(0, side, size * 2):
                draw.rectangle((j, i, j + size - 1, i + size - 1), fill=(255, 255, 255), width=size)
        f = not f
    new_image.save('board.png', 'png')


n = int(input('Введите количество клеток: '))
s = int(input('Введите размер клеток: '))
board(n, s)
