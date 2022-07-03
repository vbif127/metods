
dict_update = """

    # dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

    a = {1 : 2, 3 : 4}# a имеет тип dict(словарь)(a type dict)

    print(a)# выведется {1: 2, 3: 4}

    a.update({1: 5})

    print(a)# выведется {1: 5, 3: 4}

    a.update({5: 6})

    print(a)# выведется {1: 5, 3: 4, 5: 6}

"""


