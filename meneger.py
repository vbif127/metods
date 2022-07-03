


from list_._list import metod_list#{

from list_.list_append import list_append
from list_.list_extend import list_extend
from list_.list_insert import list_insert
from list_.list_remove import list_remove
from list_.list_pop import list_pop
from list_.list_index import list_index
from list_.list_sort import list_sort
from list_.list_count import list_count
from list_.list_reverse import list_reverse
from list_.list_copy import list_copy
from list_.list_clear import list_clear

#}

from dict_._dict import metod_dict#{

from dict_.dict_clear import dict_clear
from dict_.dict_copy import dict_copy
from dict_.dict_get import dict_get
from dict_.dict_items import dict_items
from dict_.dict_keys import dict_keys
from dict_.dict_pop import dict_pop
from dict_.dict_popitem import dict_popitem
from dict_.dict_setdefault import dict_setdefault
from dict_.dict_update import dict_update
from dict_.dict_values import dict_values

#}

from class_._class import metod_class#{




#}





g = {
    1: metod_class,
    2: metod_dict,
    3: metod_list
}

meneg_list = {
    1: list_append,
    2: list_extend,
    3: list_insert,
    4: list_remove,

    # 10.03.2022 {

    5: list_pop,
    6: list_index,
    7: list_count,
    8: list_sort,
    9: list_reverse,
    10: list_copy,
    11: list_clear

    #}
}

meneg_dict = {

    # 11.03.2022 {

    1: dict_clear,
    2: dict_copy,
    3: dict_get,
    4: dict_items,

    #}

    # 12.03.2022 {

    5: dict_keys,

    #}

    # 15.03.2022 {

    6: dict_pop,
    7: dict_popitem,
    8: dict_setdefault,

    #}

    # 16.03.2022 {

    9:dict_update,
    10:dict_values

    #}
}





user = ['1-metod_class(1-2)', '2-metod_dict', '3-metod_list']
for e in range(len(user)):
    print(user[e])
i = int(float(input('Введи номер метода:')))

# print(g[i])

if i == 3:

    print(g[i])

    #for h in user_list:

    h = int(float(input('Введи № метода(1-11):')))

    print(meneg_list[h])

elif i == 2:

    print(g[i])

    #for h in user_dict:

    h = int(float(input('Введи № метода(1-10):')))

    print(meneg_dict[h])

elif i == 1:

    h = int(float(input('1-2:')))

    print(metod_class[h-1])
# sad