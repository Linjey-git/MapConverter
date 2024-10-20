from tkinter import filedialog
from tkinter import *
from PIL import Image
import svgwrite
import numpy as np
import io


import COLOURS


def convert_png_to_svg(image, output_path):
    # Створення об'єкту svgwrite.Drawing
    dwg = svgwrite.Drawing(output_path, size=image.size)

    # Додавання картинки до SVG
    dwg.add(svgwrite.image.Image(x=0, y=0, width=image.width, height=image.height, href=image))

    # Збереження SVG у файл
    dwg.save()
    print(f"Картинка успішно конвертована в SVG та збережена у {output_path}")

def delete_black(map):
    map = map.convert("RGB")

    width, height = map.size

    # Проходимо по кожному пікселю зображення
    for x in range(width):
        for y in range(height):
            # Отримання значень кольору пікселя
            r, g, b = map.getpixel((x, y))
            # Перевірка, чи є піксель чорним
            if (r, g, b) == COLOURS.BLACK:
                # Встановлення білого кольору для чорного пікселя
                map.putpixel((x, y), COLOURS.GREEN)

    return map


def get_colours(map, max_colours):
    colours = map.getcolors(maxcolors=max_colours)
    final_colours = []

    for colour_tuple in colours:
        final_colours.append(colour_tuple[1])

    return final_colours


def convert_list_to_hsv(rgb_colours):
    hsv_colours = []
    for colour in rgb_colours:
        hsv_colours.append(COLOURS.rgb_to_hsv(colour))

    return hsv_colours


def generate_color_variations(color):
    r, g, b = color
    variations = []

    # Генеруємо кольори, що відрізняються від заданого на одиницю в кожному каналі
    for r_offset in range(-1, 2):
        for g_offset in range(-1, 2):
            for b_offset in range(-1, 2):
                new_r = max(0, min(255, r + r_offset))
                new_g = max(0, min(255, g + g_offset))
                new_b = max(0, min(255, b + b_offset))
                variations.append((new_r, new_g, new_b))

    return variations


def convert_list_to_rgb(hsv_colours):
    rgb_colours = []
    for hsv in hsv_colours:
        colour = COLOURS.hsv_to_rgb(hsv)
        rgb_colours.append(colour)
        rgb_colours.extend(generate_color_variations(colour))

    return rgb_colours


def remove_duplicates(list):
    # Створення нового списку для унікальних елементів
    unique_list = []

    # Проходження через кожен елемент вхідного списку
    for item in list:
        # Перевірка, чи елемент вже є в унікальному списку
        if item not in unique_list:
            # Якщо елемент ще не додано, додаємо його до унікального списку
            unique_list.append(item)

    return unique_list


def get_elements_at_uniform_distance(input_list, num_elements):
    # Обчислюємо крок
    step = (len(input_list) - 1) / (num_elements - 1)
    # Створюємо список індексів
    indices = [round(i * step) for i in range(num_elements)]
    # Витягуємо елементи за обраними індексами
    selected_elements = [input_list[i] for i in indices]
    return selected_elements


def split_list_into_sectors(input_list, num_sectors):
    # Знаходимо кількість елементів в кожному секторі
    sector_length = len(input_list) // num_sectors
    # Розділяємо вихідний список на сектори
    sectors = [input_list[i:i + sector_length] for i in range(0, len(input_list), sector_length)]
    # Створюємо словник для зберігання середнього значення кольору кожного сектору разом з сектором
    sectors_with_average_color = {}
    for i, sector in enumerate(sectors):
        # Знаходимо середнє значення кожного кольору у секторі
        average_color = tuple(int(sum(color) / len(color)) for color in zip(*sector))
        # Зберігаємо середнє значення кольору та сектор у словнику
        sectors_with_average_color[average_color] = sector
    return sectors_with_average_color


def divide_colors(colors, percentages):
    result = {}
    # total_sum = sum(percentages)
    color_index = 0
    start_percentage = 0

    for percentage in percentages:
        end_percentage = start_percentage + percentage
        color_section = colors[color_index:int(len(colors) * end_percentage / 100)]
        middle_color_index = int(len(color_section) / 2)
        middle_color = color_section[middle_color_index]
        result[middle_color] = color_section

        start_percentage = end_percentage
        color_index = int(len(colors) * start_percentage / 100)

    return result


def set_scalecolour_to_sector(colour_list):
    colours = colour_list.copy()

    percentages = [4, 6, 11, 12, 16, 17, 10, 10, 10]

    centres = divide_colors(colours, percentages)

    new_centres = {new_key: centres[old_key] for old_key, new_key in zip(centres.keys(), COLOURS.SCALE_COLOURS)}

    return new_centres


# def replace_colors(image, color_map):
#     # Проходження через усі пікселі зображення
#     width, height = image.size
#     for x in range(width):
#         for y in range(height):
#             # Отримання кольору пікселя
#             pixel_color = image.getpixel((x, y))
#             # Перевірка, чи є цей кольор в одному з діапазонів
#             for color, color_range in color_map.items():
#                 if pixel_color in color_range:
#                     # Заміна кольору пікселя на відповідний кольор з мапи
#                     image.putpixel((x, y), color)
#                     break  # Зупинка перевірки, якщо знайдено відповідний кольор

from PIL import Image

def replace_colors(image, color_map):
    layers = {}
    bright_green = (0, 255, 0)  # Яскраво-зелений колір
    unique_green_used = False

    # Проходження через усі пікселі зображення
    width, height = image.size
    for x in range(width):
        for y in range(height):
            # Отримання кольору пікселя
            pixel_color = image.getpixel((x, y))
            # Перевірка, чи є цей кольор в одному з діапазонів
            for color, color_range in color_map.items():
                if pixel_color in color_range:
                    # Створення шару для кожного кольору, якщо він ще не створений
                    if color not in layers:
                        layers[color] = Image.new('RGB', (width, height), (255, 255, 255))
                    # Заміна кольору пікселя на відповідний кольор з мапи у відповідному шарі
                    layers[color].putpixel((x, y), pixel_color)
                    # Перевірка, чи вже використовується унікальний зелений колір
                    if pixel_color == bright_green and not unique_green_used:
                        layers['bright_green'] = Image.new('RGB', (width, height), (255, 255, 255))
                        layers['bright_green'].putpixel((x, y), bright_green)
                        unique_green_used = True
                    break  # Зупинка перевірки, якщо знайдено відповідний кольор

    # Зберігаємо кожен шар у файл формату EPS
    for color, layer_image in layers.items():
        layer_output_path = f"{color}_layer.eps"
        layer_image.save(layer_output_path, format="EPS")
        print(f"Шар \"{color}\" збережено у файл {layer_output_path}")



def convert_map(height_path):
    height_map = Image.open(height_path)

    height_map = delete_black(height_map)

    colours = get_colours(height_map, 1024)

    if COLOURS.BLACK in colours:
        print("after getting colours")

    colours = [colour for colour in colours if colour != COLOURS.GREEN]

    # print(colours)

    # COLOURS.display_all_colours(colours)

    colours = convert_list_to_hsv(colours)
    # print("HSV: ", colours)

    colours = sorted(colours, key=lambda x: x[2])
    # print(colours)

    colours = convert_list_to_rgb(colours)
    colours = remove_duplicates(colours)
    # print("RGB - dub: ",colours)

    # COLOURS.display_all_colours(colours)

    centres = set_scalecolour_to_sector(colours)

    print(centres)
    # height_map.show()
    replace_colors(height_map, centres)
    height_map.show()
    # height_map.save('topography_map.png')
    convert_png_to_svg(height_map, 'topography_map.svg')

    # print(len(centres))


# Вибір файлу з допомогою діалогового вікна
root = Tk()
root.withdraw()
height_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
if height_path:
    convert_map(height_path)
