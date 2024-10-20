from tkinter import filedialog
from tkinter import *
from PIL import Image
import svgwrite
import numpy as np
import io
import aspose



# Вибір файлу з допомогою діалогового вікна
root = Tk()
root.withdraw()
height_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
if height_path:
    convert_map(height_path)