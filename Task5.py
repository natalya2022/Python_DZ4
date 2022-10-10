# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов. 2*x² + 4*x + 5
# 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

def file_to_dict(file_name):
    f = open(file_name, 'r')
    s = f.readline()+'*x**0'
    f.close()
    my_dict = {}
    for i in (s.split('+')):
        value, key = i.split('*x**')
        my_dict[int(key)] = int(value)
    return my_dict


a = file_to_dict('task4_a.txt')     # Файлы генерируются в предыдущей задаче
b = file_to_dict('task4.txt')
for key, value in a.items():
    if key in b:
        b[key] += a[key]
    else:
        b[key] = a[key]
s = ''
for key, value in b.items():
    if len(s):
        s += "+"
    s += str(value)
    if (key > 1):
        s += '*x**' + str(key)
    if (key == 1):
        s += '*x'
print(s)
