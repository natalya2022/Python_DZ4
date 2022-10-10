# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

from sympy import isprime

def prime_numbers(n):
    my_array = []
    for i in range(1,n):
        if isprime(i) and a%1 == 0:
            while a%1 == 0:
                my_array.append(i)
                a //=1
    return my_array
n = int(input())
print(prime_numbers(n))