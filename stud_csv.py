import csv

csv_file = []


# Открыть файл
def file_open(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))

# Добавление

def insert(bilet, fio, gender, age, tel, email, group, course):
    try:
        csv_file.append({'номер билета': bilet,
                         'фио': fio,
                         'пол': gender,
                         'возраст': age,
                         'телефон': tel,
                         'почта': email,
                         'группа': group,
                         'курс': course})
        except Exception as e:
            return f"Ошибка при добавлении записи {e}"
        print("Данные добавлены")