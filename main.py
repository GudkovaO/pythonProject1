from stud_csv import file_open, insert, show_rows, save, drop_by_arg, find, find_group

FILENAME = "data.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить студента',
    '3': 'Удалить студента',
    '4': 'Найти студента по ФИО',
    '5': 'Вывести студентов из группы',
    '6': 'Перевод студентов',
    '7': 'Вывести студентов старше 18',
    '8': 'Вывести данные о студенте',
    '9': 'Сохранить в файл',
    '10': 'Вывести все записи',
    '0': '<- Меню',
    'exit': 'Выход'
}
for k, v in MENU.items():
    print(k, '-', v)

while True:
    action = input('>_')
    if action == '1':
        file_open(FILENAME)

    elif action == 'exit':
        break
 elif action == '2':
        insert(input('Номер билета: '), input('ФИО: '), input('Пол: '), input('Возраст: '), input('Телефон: '),
               input('Почта: '), input('Группа: '), input('Курс: '))
elif action == '3':
print(drop_by_arg(input("Значение: "), input("Колонка: ")))
elif action == '4':
find(input("Значение: "), input("Колонка: "))
elif action == '5':
find_group(input("Значение: "), input("Колонка: "))
elif action == '9':
save()
elif action == '10':
show_rows()
elif action == '0':
for k, v in MENU.items():
    print(k, '-', v)
elif action == 'exit':
break