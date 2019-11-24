from PIL import Image, ImageDraw


def gradient_with_line(color):
    new_image = Image.new('RGB', (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    cl = 0
    for i in range(0, 512, 2):
        if color == 'R':
            draw.line(((i, 0), (i, 200)), fill=(cl, 0, 0), width=2)
        elif color == 'G':
            draw.line(((i, 0), (i, 200)), fill=(0, cl, 0), width=2)
        elif color == 'B':
            draw.line(((i, 0), (i, 200)), fill=(0, 0, cl), width=2)
        cl += 1
    new_image.save('gradient.png', 'PNG')


gradient_with_line('R')
