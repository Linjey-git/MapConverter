from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageFilter
import numpy as np

def map_colors(image_path):
    try:
        # Відкриття зображення
        image = Image.open(image_path)
        # Перевірка формату
        if image.format == "PNG":
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
        else:
            print("Обраний файл не є PNG зображенням.")
    except Exception as e:
        print("Помилка:", e)





# Виклик функції з шляхом до вашого зображення
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
if image_path:
    map_colors(image_path)