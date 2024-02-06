import csv

# Чтение меток из файла
path_to_file = 'G:\chertila_NN\lo_spec\labels.txt'
with open(path_to_file, 'r', encoding = 'utf-8') as file:
    lines = file.readlines()

# Создание CSV-файла и запись данных
with open('G:\chertila_NN\lo_spec\labels.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Изображение', 'Текст'])

    for line in lines:
        parts = line.strip().split(': ', maxsplit=1)
        image_name = parts[0]
        text = parts[1]
        csv_writer.writerow([image_name, text])
