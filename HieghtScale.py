from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageFilter

def map_colors(image_path):
    # try:
        # Відкриття зображення
        image = Image.open(image_path)
        # Перевірка формату зображення
        if image.format == "PNG":
            # Розбиття діапазону кольорів на 10 позицій
            color_range = [(0, 128, 0), (34, 139, 34), (60, 179, 60), (84, 208, 84),
                           (120, 230, 120), (170, 255, 170), (204, 255, 204), (230, 255, 230),
                           (245, 255, 245), (255, 255, 255)]
            # Конвертація зображення в режим "L" (відтінки сірого)
            gray_image = image.convert("L")
            gray_image.show()
            # Нормалізація значень пікселів в діапазон від 0 до 9
            normalized_image = gray_image.point(lambda p: int(p / 25.5))
            # Заміна кожного пікселя на відповідний кольор з діапазону
            mapped_image = normalized_image.point(lambda p: color_range[p])
            # Відображення зображення після обробки
            mapped_image.show()
        else:
            print("Обраний файл не є PNG зображенням.")
    # except Exception as e:
    #     print("Помилка:", e)

# Вибір файлу з допомогою діалогового вікна
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
if image_path:
    map_colors(image_path)