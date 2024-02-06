import os
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Model


# Функция для One-Hot Encoding
def one_hot_encode(text, charset):
    char_to_int = {char: i for i, char in enumerate(charset)}
    integer_encoded = [char_to_int[char] for char in text]

    onehot_encoded = np.zeros((len(text), len(charset)))
    for i, value in enumerate(integer_encoded):
        onehot_encoded[i][value] = 1

    return onehot_encoded


# Загрузка меток и изображений
labels_df = pd.read_csv('G:\chertila_NN\lo_spec\labels.csv', encoding='windows-1251')
charset = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890-.,:;"

images = []
labels = []

for _, row in labels_df.iterrows():
    image_path = 'G:\chertila_NN\lo_spec\images' + f'\{row["Изображение"]}'
    image = cv2.imread(image_path)
    image = cv2.resize(image, (300, 300))
    image = image / 255.0
    images.append(image)

    encoded_label = one_hot_encode(str(row["Текст"]), charset)  # Преобразование метки в строку перед кодированием
    labels.append(encoded_label)

images = np.array(images)
labels = np.array(labels)

# Разделение набора данных на обучающий и тестовый
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Создание нейронной сети
input_layer = Input(shape=(300, 300, 3))
x = Conv2D(32, (3, 3), activation='relu')(input_layer)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(128, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Flatten()(x)
x = Dense(256, activation='relu')(x)
output_layer = Dense(len(charset), activation='softmax')(x)

model = Model(input_layer, output_layer)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Обучение нейронной сети
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
