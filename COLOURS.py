import colorsys
import math
from PIL import Image


def rgb_to_hsv(rgb):
    # Розпаковуємо значення R, G, B з кортежу та нормалізуємо до діапазону [0, 1]
    r, g, b = [x / 255.0 for x in rgb]
    # Конвертуємо RGB у HSV
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    # Перетворюємо значення H з діапазону [0, 1] у [0, 360] і округлюємо до цілого числа
    h = h * 360
    # Перетворюємо значення S та V з діапазону [0, 1] у [0, 100] і округлюємо до цілого числа
    s = s * 100
    v = v * 100
    # Повертаємо HSV кортеж з цілими значеннями
    return (h, s, v)


def hsv_to_rgb(hsv):
    # Розпаковуємо значення H, S, V з кортежу
    h, s, v = hsv
    # Перетворюємо значення H, S, V з діапазону [0, 360] та [0, 100] у [0, 1]
    h /= 360.0
    s /= 100.0
    v /= 100.0
    # Конвертуємо HSV у RGB
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    # Перетворюємо значення RGB з діапазону [0, 1] у [0, 255] і округлюємо до цілого числа
    r = r * 255
    g = g * 255
    b = b * 255
    # Повертаємо RGB кортеж з цілими значеннями
    return (int(r), int(g), int(b))


def display_all_colours(colours_list):
    square_size = 67

    colours = colours_list.copy()

    new_square = Image.new("RGB", (square_size, square_size))

    # Заповніть кожен піксель кольором зі списку унікальних кольорів
    for y in range(square_size):
        for x in range(square_size):
            # Отримайте наступний унікальний колір зі списку
            if colours:
                colour = colours.pop(0)
                # Встановіть колір пікселя
                new_square.putpixel((x, y), colour)

    new_square.show()


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0, 255)
YELLOW_water = (255, 255, 84, 255)
CYAN = (0, 255, 255, 255)
MAGENTA = (255, 0, 255)
TRANSPARENT = (0, 0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# scale
COLOUR_0 = (19, 108, 122)
COLOUR_100 = (72, 135, 140)
COLOUR_200 = (125, 161, 157)
COLOUR_350 = (177, 188, 175)
COLOUR_600 = (228, 215, 193)
COLOUR_1000 = (199, 155, 138)
COLOUR_1500 = (169, 95, 83)
COLOUR_2500 = (191, 191, 191)
COLOUR_4000 = (244, 243, 241)

SCALE_COLOURS = [COLOUR_0, COLOUR_100, COLOUR_200, COLOUR_350, COLOUR_600, COLOUR_1000, COLOUR_1500, COLOUR_2500,
                 COLOUR_4000]
