#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def find_max_len(word_list):
    max_result = 0
    for word_l in word_list:
        if max_result < len(word_l):
            max_result = len(word_l)
    return max_result


def text2png(text, fullpath, color="#FFF", bgcolor="#300A24", fontfullpath=None, fontsize=15,
             leftpadding=10, rightpadding=3, width=600):
    if fontfullpath is None:
        font = ImageFont.load_default()
    else:
        ImageFont.truetype(fontfullpath, fontsize)
    lines = []
    words = text.split()
    max_len = find_max_len(words)

    line = u" " + " "*max_len
    for word in words:
        if font.getsize(line + ' ' + word)[0] <= (width - rightpadding - leftpadding):
            if ':' in word:
                lines.append(line[1:])  # slice the white space in the begining of the line
                line = u""
            else:
                line += u''
            line += '  ' + ' '*(max_len - len(word)-1) + word

    if len(line) != 0:
        lines.append(line[1:])
    line_height = font.getsize(text)[1] * 2
    img_height = line_height * (len(lines) + 1)
    img = Image.new("RGBA", (width, img_height), bgcolor)
    draw = ImageDraw.Draw(img)

    y = 0
    for line in lines:
        draw.text((leftpadding, y), line, color, font=font)
        y += line_height
    img.save(fullpath)
    return fullpath
