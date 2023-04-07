# Задача 34: 
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку  разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам  стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число  гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного  слова, если во фразе несколько слов, то они разделяются дефисами. Фразы 
# отделяются друг  от друга пробелами.  Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе 
# напишите “Парам пам-пам”, если с ритмом  все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:  пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам

# str_1 = input('Введите стихотворение: ').split()
# print(str_1)
# volwel_letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
# rhythm = list()
# for phrase in str_1:
#     count_vowel_letters = 0
#     for letter in phrase:
#         if letter in volwel_letters:
#             count_vowel_letters +=1
#     rhythm.append(count_vowel_letters)
#     # print(count_vowel_letters)
# if len(set(rhythm))== 1:
#     print('Парам пам-пам')
# else:
#     print('Пам па-рам')        

# через функцию

str_1 = input('Введите стихотворение: ').split()
print(str_1)
def rhythm(str):
    list_1 = []
    for phrase in str:
        count_vowel_letters = 0
        for letter in phrase:
            if letter in 'аеёиоуыэюя':
                count_vowel_letters += 1
        list_1.append(count_vowel_letters)
    return len(list_1) == list_1.count(list_1[0])

if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')




# Задача 36: 
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: 
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36 


# def print_operation_table(operation, num_rows = 6, num_columns = 6): 
# num_rows = 6
# num_columns = 6
# operation = [[i]*num_columns for i in range(num_rows)]
# for i in operation:
#     print(i)


    