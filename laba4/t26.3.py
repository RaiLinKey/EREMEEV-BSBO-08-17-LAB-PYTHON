from PIL import Image


def make_anagliph(filename, delta):
    image_1 = Image.open(filename)
    image_2 = image_1.copy()
    pix = image_1.load()
    pix_c = image_2.load()
    x, y = image_1.size
    for i in range(delta, x):
        for j in range(y):
            r, g, b = pix[i, j]
            pix[i, j] = pix_c[i - delta, j][0], g, b
    image_1.save('stereo.png', 'PNG')


make_anagliph('test.jpg', 15)
