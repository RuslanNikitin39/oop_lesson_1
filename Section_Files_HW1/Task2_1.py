from pprint import pprint
import os

def read_cook_book():
    path = os.path.join(os.getcwd(), 'recipes.txt')

    with open(path, encoding='utf-8') as file:
        cook_book = {}
        for recipe in file:
            cook_name = recipe.strip()
            num_ingredients = int(file.readline().strip())
            temp_data = []
            for item in range(num_ingredients):
                ingredient_name, quantity, measure = file.readline().strip().split('|')
                temp_data.append(
                    {'ingredient_name' : ingredient_name, 'quantity' : int(quantity), 'measure' : measure}
                )
            cook_book[cook_name] = temp_data
            file.readline()

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book()
    temp_dict = {}
    for item in dishes:
        if not item in cook_book.keys():
            continue
        dish = cook_book[item]
        for ingridient in dish:
            key = ingridient['ingredient_name']
            if not key in temp_dict:
                temp_dict.setdefault(key, {'measure': ingridient['measure'], 'quantity' : 0})
            temp_dict[key]['quantity'] += ingridient['quantity'] * int(person_count)
    pprint(temp_dict)

def join_files():
    files = []
    files.append('1.txt')
    files.append('2.txt')
    files.append('3.txt')

    temp_data = []
    for f_name in files:
        file_name = f_name
        with open(os.path.join(os.getcwd(), f_name), encoding='utf-8') as file:
            text = file.readlines()
            size = len(text)
        temp_data.append({'name' : file_name, 'size' : size, 'text' : text})
    newlist = sorted(temp_data, key=lambda k: k['size'])

    # pprint(newlist)

    path = os.path.join(os.getcwd(), '4.txt')
    with open(path, 'w', encoding='utf-8') as w_file:
        for item in newlist:
            w_file.write(f"{item['name']}\n")
            w_file.write(f"{item['size']}\n")
            for el in item['text']:
                w_file.write(f'{el.strip()}\n')

def main():
    # Задача 1: вывод словаря из файла
    print('Решение задачи 1:\n')
    cook_book = read_cook_book()
    pprint(cook_book)
    print()

    # Задача 2: рассчет количества ингридиентов
    print('Решение задачи 2:\n')
    dishes = []
    dishes.append('Запеченный картофель')
    dishes.append('Фахитос')
    dishes.append('Омлет1')
    dishes.append('Омлет')
    get_shop_list_by_dishes(dishes, 2)
    print()

    # Задача 3: объединение файлов
    print('Решение задачи 3:\n')
    join_files()

main()