def read_file(path):
    cook_book = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            name = line.strip().lower()
            cook_book[name] = []
            count = f.readline()
            for number in range(int(count)):
                ingredient_list = f.readline().strip().split("|")
                ingredients_dict = {"ingredient_name": ingredient_list[0],
                                    "quantity": int(ingredient_list[1]),
                                    "measure": ingredient_list[2]}
                cook_book[name].append(ingredients_dict)
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file("cook_book.txt")
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list = dict(ingredient)
            new_shop_list["quantity"] *= person_count
            if new_shop_list['ingredient_name'] not in shop_list:
                shop_list[new_shop_list['ingredient_name']] = {"measure": new_shop_list["measure"], "quantity": new_shop_list["quantity"]}
            else:
                shop_list[new_shop_list['ingredient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list


def start():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите список блюд (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print(shop_list)


start()
