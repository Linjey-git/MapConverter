import colorsys

import COLOURS


def rgb_to_hsv(rgb):
    # Розпаковуємо значення R, G, B з кортежу та нормалізуємо до діапазону [0, 1]
    r, g, b = [x / 255.0 for x in rgb]
    # Конвертуємо RGB у HSV
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    # Перетворюємо значення H з діапазону [0, 1] у [0, 360] і округлюємо до цілого числа
    h = round(h * 360)
    # Перетворюємо значення S та V з діапазону [0, 1] у [0, 100] і округлюємо до цілого числа
    s = round(s * 100)
    v = round(v * 100)
    # Повертаємо HSV кортеж з цілими значеннями
    return (int(h), int(s), int(v))



print(rgb_to_hsv(COLOURS.GREEN))
