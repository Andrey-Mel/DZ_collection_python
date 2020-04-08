import random
from collections import Counter
from datetime import datetime

list_name = ['Пётр', 'Емельян', 'Зенон', 'Устин', 'Цицерон', 'Роман', 'Цезарь', 'Ян', 'Эрик', 'Жерар', 'Даниил', \
             'Арсений', 'Родион', 'Клим', 'Павел', 'Яков', 'Чеслав', 'Марк', 'Шерлок', 'Нестор']
N = 100


#
# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
#
def f_more_name(name, x):
    new_list_name = random.choices(name, k=x)
    return new_list_name


#
##print(f_more_name(list_name, N))
#
# Напишите функцию вывода самого частого имени из списка на выходе функции F
#
list_sort_name = f_more_name(list_name, N)


def func_name(list_name):
   name = Counter(list_sort_name)
   max_counter = max(name.values())
   max_name = list(word for word, count in name.items() if count == max_counter)
   return max_name


#print(func_name(list_sort_name))


#
## Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
#
def func_letter(names_list):
   name_count = Counter(list_sort_name)
   name = min(name_count.items(), key=lambda x: x[1])#[0]
   return name


#print(func_name(list_sort_name))

#
##Задание  для pro: В файле с логами найти дату самого позднего лога (по метке времени):
#
with open("log", 'r') as f:
    date_time_min = 0
    for line in f:
        if not date_time_min:
            date_time_min = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
            continue
            date_time_max = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
            if date_time_max < date_time_min:
                date_time_min = date_time_max
    print(date_time_min)
