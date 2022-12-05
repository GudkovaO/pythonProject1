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
# Удаление
def drop_by_arg(val, col_name="номер билета"):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f"Строка со значением {val} поля {col_name} не найдена"
    return f"Строка со значением {val} поля {col_name} удалена"


# Поиск по ФИО
def find(val, col_name="фио"):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))
