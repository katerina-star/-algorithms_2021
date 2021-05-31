"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple


firm_inc = namedtuple('Income', 'name income_1 income_2 income_3 income_4')
n = int(input('Введите количество предприятий для расчета прибыли: '))


def count_profit(n, m=1, sum_all=0, aver_inc=0, firms=None):
    if firms is None:
        firms = {}
    c = firm_inc(input('Введите название предприятия: '),
                 *[int(i) for i in input('через пробел введите прибыль '
                                         'данного предприятия за каждый '
                                         'квартал(Всего 4 квартала): ').split(' ')])
    sum_1 = c.income_1 + c.income_2 + c.income_3 + c.income_4
    sum_all = sum_all + sum_1
    firms[c.name] = sum_1   # сохраняет в словарь доход каждой фирмы чтобы сравнивать потом
    if m == n:
        aver_inc = round(sum_all/n, 1)
        print(f'Средняя годовая прибыль всех предприятий: '
              f'{aver_inc}')
        count_up_down(aver_inc, firms)
        return
    count_profit(n, m+1, sum_all, aver_inc, firms)


def count_up_down(aver, firms):
    """сравнивает доход каждой фирмы со средним"""
    if not firms:
        return
    f_inc = firms.popitem()
    if f_inc[1] < aver:
        print(f'Предприятия, с прибылью ниже среднего значения: {f_inc[0]}')
    if f_inc[1] > aver:
        print(f'Предприятия, с прибылью выше среднего значения: {f_inc[0]}')
    return count_up_down(aver, firms)


count_profit(n)
