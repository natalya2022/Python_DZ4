# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

my_arr = [1, 5, 7, 3, 8, 5, 1, 5]
my_dict = {}
for i in my_arr:
    if i in my_dict:
        my_dict[i] +=1
    else:
        my_dict[i] = 1
for key, value in my_dict.items():
    if value < 2:
        print(key, end=' ')
   
