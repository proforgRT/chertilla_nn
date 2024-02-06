import random
import string
from PIL import Image, ImageDraw, ImageFont
import os


# Создаем функцию для генерации случайной строки на русском языке с использованием специальных символов и различных регистров
def generate_random_russian_text(length):
    russian_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    russian_digits = "1234567890"
    punctuation_symbols = "-.,:;"
    russian_chars = russian_lowercase + russian_uppercase + russian_digits + punctuation_symbols
    return ''.join(random.choice(russian_chars) for _ in range(length))


# Создаем функцию для генерации изображения с текстом
def create_image_with_text(text, font_path, image_size, output_path):
    image = Image.new("RGB", image_size, color="white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, 30,)

    text_width, text_height = draw.textsize(text, font)
    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2

    draw.text((text_x, text_y), text, font=font, fill="black")
    image.save(output_path)


# Указываем путь к шрифту
font_path = "G:\chertila_NN\italicfont.ttf"

# Создаем директорию для сохранения изображений и файл с метками
output_directory = "G:\chertila_NN\lo_spec"
labels_file_path = "G:\chertila_NN\lo_spec\labels.txt"
# Генерируем изображения с текстом и сохраняем метки
image_count = 500000  # Количество изображений для генерации
image_size = (300, 300)  # Размеры изображений

with open(labels_file_path, 'w', encoding='utf-8') as labels_file:
    for i in range(image_count):
        random_text_length = random.randint(5, 20)  # Генерируем случайную длину текста от 5 до 20 символов
        random_text = generate_random_russian_text(random_text_length)
        output_path = os.path.join(output_directory + '\images', f"image_{i + 1}.png")
        create_image_with_text(random_text, font_path, image_size, output_path)

        # Сохраняем метку в файл
        labels_file.write(f"image_{i + 1}.png: {random_text}\n")
