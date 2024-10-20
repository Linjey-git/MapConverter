from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageFilter


def remove_gradient(image_path):
    try:
        # Відкриття зображення
        image = Image.open(image_path)
        # Перевірка формату зображення
        if image.format == "PNG":
            # Застосування медіанного фільтру для видалення градієнтів
            denoised_image = image.filter(ImageFilter.MedianFilter(size=5))
            # Відображення зображення після обробки
            denoised_image.show()
            # remove_gradient(image_path)
        else:
            print("Обраний файл не є PNG зображенням.")
    except Exception as e:
        print("Помилка:", e)


# Вибір файлу з допомогою діалогового вікна
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
if image_path:
    remove_gradient(image_path)
