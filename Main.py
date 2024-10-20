from tkinter import filedialog
from tkinter import *
from PIL import Image

def count_colors_and_rgb():
    try:
        # Відкриття файлу за допомогою діалогового вікна
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        # Перевірка, чи файл обраний та чи це PNG зображення
        if file_path:
            image = Image.open(file_path)
            # image.show()
            if image.format == "PNG":
                # Конвертація до формату "RGB", щоб мати змогу підрахувати кольори
                image = image.convert("RGB")
                # image.show()
                # Отримання списку унікальних кольорів та їх кількості
                colors = image.getcolors(maxcolors=8192)
                print("after list")
                print(colors)
                # Підрахунок кількості унікальних кольорів
                num_colors = len(colors)

                # Виведення кількості та RGB значень кольорів
                print("Кількість унікальних кольорів на зображенні:", num_colors)
                print("RGB значення кольорів:")
                for color in colors:
                    print("RGB:", color[1])
            else:
                print("Обраний файл не є PNG зображенням.")
        else:
            print("Файл не обраний.")
    except Exception as e:
        print("Помилка:", e)

count_colors_and_rgb()