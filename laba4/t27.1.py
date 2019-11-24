from PIL import Image


def make_preview(size, n_colors):
    i_convert = Image.open('test.jpg')
    i_convert.thumbnail(size)
    i_convert = i_convert.convert('P', palette=Image.WEB, colors=n_colors)
    i_convert.save('res2.bmp', 'BMP')


make_preview((900, 500), 64)
