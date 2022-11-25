import datetime

import pandas

csv_file = None
menu = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по значению',
    '5': 'Вывести средний возраст',
    '6': 'Сохранить в файл',
    '7': 'Вывести в алфавитном порядке товары',
    '0': '<-Меню',
    'exit': 'Выход'
}


def file_open():
    try:
        data = pandas.read_csv('data.csv', delimiter=";")
    except Exception as e:
        print(e)
    print('Файл открыт. Записей:', len(data.index))
    return data


def insert(product, price, quantity, discount, measurements, date):
    global csv_file
    df_insert = pandas.DataFrame([(max(csv_file['номер'] + 1), product, price, quantity, discount, measurements, date)],
                                 columns=('товар', 'цена', 'количество', 'скидка', 'ед. измерения', 'дата продажи'))
    df2 = pandas.concat([csv_file, df_insert])
    return df2


def drop_by_arg(val, col_name='товар'):
    global csv_file
    if col_name == 'номер' or col_name == 'цена':
        val = int(val)
    csv_file = csv_file.set_index(col_name)
    csv_file.drop(val, axis=0, inplace=True)
    print(csv_file)


def find(val, col_name='товар'):
    df = csv_file[csv_file[col_name].isin([val])]
    print(df)


def avg_age():
    print("Средний возраст:", csv_file["возраст"].mean())


def save():
    try:
        csv_file.to_csv('data.csv', index=False, sep=';')
    except Exception as e:
        print(e)


def biggest(price):
    df = csv_file[csv_file[price].max([val])]
    print(df)








# Вывод меню
print('\n'.join([f"{k} : {v}" for k, v in menu.items()]))
while True:
    comand = input()
    if comand == '1':
        csv_file = file_open()
    elif comand == '2':
        csv_file = insert(input('Товар: '), int(input('Цена: ')),
                         int(input('Количество: ')),  int(input('Скидка: ')),
                         input('Ед. измерения: '), int(input('Дата продажи: ')))
        print(csv_file)
    elif comand == '3':
        col = input('Колонка: ')
        val = input('Значение: ')
        drop_by_arg(val, col_name=col)
    elif comand == '4':
        col = input('Колонка: ')
        val = input('Значение: ')
        find(val, col_name=col)
    elif comand == '5':
        avg_age()
    elif comand == '6':
        save()
    elif comand == '7':

    elif comand == '0':
        print('\n'.join([f"{k} : {v}" for k, v in menu.items()]))
    else:
        break