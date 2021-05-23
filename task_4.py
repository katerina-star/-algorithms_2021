"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib

tabl_adr = dict()


def ad_addr(dic):
    url_addr = input('Вставьте адрес страницы: ')
    if url_addr == '':
        return dic
    salt = url_addr
    hash_url = hashlib.sha256(url_addr.encode() + salt.encode()).hexdigest()
    if hash_url not in dic.keys():
        dic.update({hash_url: url_addr})
    return ad_addr(dic)


print(ad_addr(tabl_adr))
