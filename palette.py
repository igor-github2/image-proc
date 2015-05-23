#!/usr/bin/env python2

import sys
from colorthief import ColorThief
from PIL import Image, ImageDraw


OFFSET = 10
OUTLINE = 'black'

color_thief = ColorThief(sys.argv[1])
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=int(sys.argv[2]))
im = Image.open(sys.argv[1])
draw = ImageDraw.Draw(im, 'RGBA')

palette.insert(0, dominant_color)

for index, p in enumerate(palette):
    _outline = OUTLINE
    if index is 0:
        _outline = 'red'
    dot = (100 * index) + OFFSET
    dot2 = 100 * (index + 1)
    dim = [(dot, 10), (dot2, 10), (dot2, 100), (dot, 100)]
    draw.polygon(dim, fill=p, outline=_outline)
    print(index, dot, dot2)

print(dominant_color)
print(palette)
print(len(palette))

im.show()
im.save('/tmp/test.png', 'PNG')
