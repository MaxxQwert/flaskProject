from PIL import Image, ImageStat, ImageColor
import numpy as np

im = Image.open('test3.jpg')
im_width, im_height = im.size
color_search = input('Input color: ')
color_rgb = ImageColor.getrgb(color_search)
count_w = 0
count_b = 0
count_color  = 0
col =set()
for x in range(im_width):
    for y in range(im_height):
        px = im.load()[x, y]
        if px == (0, 0, 0):
            count_b += 1
        elif px == (255, 255, 255):
            count_w += 1
        if px == color_rgb:
            count_color += 1
        col.update(px)
print('color white ', count_w, 'color black ', count_b, 'color cearch ', count_color)
print(color_rgb, col)
