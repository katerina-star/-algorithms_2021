"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import time

lst = []
dic = dict()


def measure(func):
    def measure_one(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения ф-ции {func.__name__} - {end - start}')
        return result

    return measure_one


@measure
def fil_lst_range(n):
    l = list(range(n))  # Сложность операции О(1)
    return


@measure
def fil_lst_compr(n):
    l = [i for i in range(n)]  # Сложность операции О(1)
    return


@measure
def fil_lst_append(n, l):
    for i in range(n):
        l.append(i)  # Сложность операции О(1)
    return


@measure
def fil_lst_insert(n, l):
    for i in range(n):
        l.insert(0, i)  # Сложность операции О(n)
    return


@measure
def fil_dic_cycl(n, d):
    for i in range(n):
        d[i] = i  # Сложность операции О(1)
    return


@measure
def fil_dic_compr(n):
    d = {i: i for i in range(n)}  # Сложность операции О(1)
    return


@measure
def pop_from_lst(ls, n):
    for i in range(n):
        ls.pop()  # Сложность операции О(1)
    return


@measure
def popitem_dict(d, n):
    for i in range(n):
        d.popitem()  # Сложность операции О(1)
    return


@measure
def popitem_from_list(ls, n):
    for i in range(n):
        ls.pop(0)  # Сложность операции О(n)
    return


@measure
def pop_from_dict(d, n):
    for i in range(n):
        d.pop(i)  # Сложность операции О(1)
    return


n = 100000
fil_dic_compr(n)
fil_dic_cycl(n, dic)
fil_lst_insert(n, lst)
fil_lst_append(n, lst)
fil_lst_compr(n)
fil_lst_range(n)
print('Вывод:\nЗаполнение списка и словаря через list/dict compr и \n'
      'list(range(n)) - самые быстрые варианты\n'
      'заполнение списка путем вставки элемента по индексу - самый медленный\n'
      '(т.к. все элементы передвигаются,\n'
      'меняя свои индексы), если его не использовать,\n'
      'то заполнение списка будет почти в два раза быстрее заполнения словаря,\n'
      'потому что при заполнении словаря происходит хеширование ключей')
print('-' * 100)
pop_from_lst(lst, n)
popitem_dict(dic, n)
print('Вывод:\n'
      'Удаление элементов с конца списка/словаря происходит быстрее в списках\n'
      'примерно в два раза')

lst = [i for i in range(n)]
dic = {i: i for i in range(n)}
print('-' * 100)
popitem_from_list(lst, n)
pop_from_dict(dic, n)
print('Вывод:\n'
      'А удаление элементов с начала списка/словаря происходит быстрее в словарях\n'
      'и разница по времени значительна')
