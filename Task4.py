# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

s = ''
k = 5
for i in range(k):
    random_number = random.randint(0, 100)
    print(random_number)
    if random_number > 0:
        if len(s):
            s += "+"
        s += str(random_number)+'*x**' + str(k-i)
random_number = random.randint(0, 100)
if random_number > 0:
    s += '+' + str(random_number)
print(s)
f = open('task4_a.txt', 'w')
f.write(s)
f.close()
