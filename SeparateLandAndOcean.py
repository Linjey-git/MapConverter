from tkinter import filedialog
from tkinter import *
from PIL import Image

import COLOURS


def map_colours(image):
    # Конвертація до формату "RGB"
    image = image.convert("RGB")
    # Отримання списку унікальних кольорів
    colors = image.getcolors(maxcolors=8192)
    # Поділ кольорів на 10 секцій
    num_sections = 10
    section_size = len(colors) // num_sections
    # Список з 10 визначених кольорів
    predefined_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0),
                         (0, 255, 255), (0, 0, 255), (128, 0, 128), (255, 0, 255),
                         (128, 128, 128), (255, 255, 255)]
    # Створення мапи кольорів
    color_map = {}
    for i in range(num_sections):
        for j in range(section_size):
            if i * section_size + j < len(colors):
                color_map[colors[i * section_size + j][1]] = predefined_colors[i]
    # Заміна кольорів у зображенні
    new_image = Image.new("RGB", image.size)
    for x in range(image.width):
        for y in range(image.height):
            pixel_color = image.getpixel((x, y))
            new_image.putpixel((x, y), color_map.get(pixel_color, (0, 0, 0)))
    # Відображення нового зображення
    new_image.show()


def display_all_colours(colours):
    square_size = 67

    new_square = Image.new("RGB", (square_size, square_size))

    # Отримайте список унікальних кольорів
    # unique_colours = list(set(colours))

    # print(unique_colours)

    # Заповніть кожен піксель кольором зі списку унікальних кольорів
    for y in range(square_size):
        for x in range(square_size):
            # Отримайте наступний унікальний колір зі списку
            if colours:
                colour = colours.pop(0)
                # Встановіть колір пікселя
                new_square.putpixel((x, y), colour)

    new_square.show()


def separate_land_and_water(topography_path, height_path):
    # Відкриття зображення
    image = Image.open(topography_path)

    # Конвертація зображення до режиму "RGB"
    rgb_image = image.convert("RGB")

    # Визначення порогових значень для висот
    water_threshold = 200  # Порогове значення для води (низькі висоти)
    land_threshold = 100  # Порогове значення для суходолу (високі висоти)

    # Створення маски для води та суходолу
    water_mask = rgb_image.point(lambda p: 255 if p < water_threshold else 0)
    land_mask = rgb_image.point(lambda p: 255 if p > land_threshold else 0)

    # Відображення масок води та суходолу
    # water_mask.show("water")  # yellow water
    # land_mask.show("land")  # green&yellow landmass

    image_rgba = image.convert("RGBA")
    water_rgba = water_mask.convert("RGBA")
    land_rgba = land_mask.convert("RGBA")

    width, height = image_rgba.size

    for x in range(width):
        for y in range(height):
            land_pixel = land_rgba.getpixel((x, y))
            water_pixel = water_rgba.getpixel((x, y))

            if water_pixel == COLOURS.YELLOW:
                image_rgba.putpixel((x, y), COLOURS.TRANSPARENT)

            if land_pixel == COLOURS.CYAN:
                image_rgba.putpixel((x, y), COLOURS.TRANSPARENT)

    image_rgba.show()

    # grey = image_rgba.convert("L")
    #
    # grey.show()

    map_without_ocean = image_rgba.copy()
    map_without_ocean = map_without_ocean.convert("RGB")
    colours = map_without_ocean.getcolors(maxcolors=8192)

    # print(colours)

    final_colours = []

    for colour_tuple in colours:
        final_colours.append(colour_tuple[1])
    print(final_colours)

    hsv_colours = []
    for colour in final_colours:
        hsv_colours.append(COLOURS.rgb_to_hsv(colour))

    print(hsv_colours)

    # hsv_colours = list(set(hsv_colours))

    hsv_colours = sorted(hsv_colours, key=lambda x: x[2])
    print(hsv_colours)

    rgb_colours = []
    for hsv in hsv_colours:
        rgb_colours.append(COLOURS.hsv_to_rgb(hsv))

    # print(rgb_colours)

    display_all_colours(rgb_colours)

# display_all_colours(final_colours)


# final_list = np.array(final_colours)
# centres = ColourClusteringAlgorithm.kmeans(final_list, 10).tolist()
# # print(centres)
# print(centres)
#
# centres = [tuple(sublist) for sublist in centres]
# centres = [(int(x), int(y), int(z)) for x, y, z in centres]
#
# print(centres)
#
# display_all_colours(centres)

# # Підрахунок кількості унікальних кольорів
# num_colours = len(colours)
#
# # Виведення кількості та RGB значень кольорів
# print("Кількість унікальних кольорів на зображенні:", num_colours)
#
# for colour in colours:
#     print("RGB:", colour[1])


# Вибір файлу з допомогою діалогового вікна
root = Tk()
root.withdraw()
topography_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
height_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
if topography_path and height_path:
    separate_land_and_water(topography_path, height_path)
