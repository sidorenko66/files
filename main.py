from pprint import pprint

def read_catalog(file_name):
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            for _ in range(int(file.readline())):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                cook_book[dish].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    cook_book = read_catalog('recipes.txt')
    for dish in dishes:
        if dish not in cook_book:
            print(f'Ошибка! Нет блюда "{dish}"!')
            continue
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in result:
                result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                result[ingredient['ingredient_name']] = {}
                result[ingredient['ingredient_name']]['quantity'] = ingredient['quantity'] * person_count
                result[ingredient['ingredient_name']]['measure'] = ingredient['measure']
    return result


def write_file(files):
    result = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            text = f.readlines()
            result.append([len(text), file, text])
    result.sort()
    with open('result.txt', 'a') as f:
        for lenght, name, text in result:
            f.write(f'{name}\n{lenght}\n')
            for line in text:
                f.write(line)
            f.write('\n')


pprint(read_catalog('recipes.txt'))
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
write_file(['1.txt', '2.txt', '3.txt'])