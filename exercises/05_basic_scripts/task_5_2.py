# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
masks = {
    '0': '0.0.0.0',
    '1': '128.0.0.0',
    '2': '192.0.0.0',
    '3': '224.0.0.0',
    '4': '240.0.0.0',
    '5': '248.0.0.0',
    '6': '252.0.0.0',
    '7': '254.0.0.0',
    '8': '255.0.0.0',
    '9': '255.128.0.0',
    '10': '255.192.0.0',
    '11': '255.224.0.0',
    '12': '255.240.0.0',
    '13': '255.248.0.0',
    '14': '255.252.0.0',
    '15': '255.254.0.0',
    '16': '255.255.0.0',
    '17': '255.255.128.0',
    '18': '255.255.192.0',
    '19': '255.255.224.0',
    '20': '255.255.240.0',
    '21': '255.255.248.0',
    '22': '255.255.252.0',
    '23': '255.255.254.0',
    '24': '255.255.255.0',
    '25': '255.255.255.128',
    '26': '255.255.255.192',
    '27': '255.255.255.224',
    '28': '255.255.255.240',
    '29': '255.255.255.248',
    '30': '255.255.255.252',
    '31': '255.255.255.254',
    '32': '255.255.255.255'
        }
ip_temp = input('Введите IP адрес в формате: 10.1.1.0/24: ')
ip_temp = ip_temp.split('/')
ip = ip_temp[0]
ip = ip.split('.')
oct1, oct2, oct3, oct4 = ip
mask = ip_temp[1]
mask_tmp = masks[mask]
mask_tmp = mask_tmp.split('.')
msk1,msk2,msk3,msk4 = mask_tmp
ip_template = '''
    Network:
    {0:10} {1:10} {2:10} {3:10}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''
mask_template = '''
    {0:10} {1:10} {2:10} {3:10}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''
print(ip_template.format(int(oct1), int(oct2), int(oct3), int(oct4)))
print('Mask:')
print('/' + mask)
print(mask_template.format(int(msk1), int(msk2), int(msk3), int(msk4)))
   
