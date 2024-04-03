#v1
# def sum_numbers(n, y = 'bye-bye'):
#     print(y)
#     res = 0
#     for i in range(1, n + 1):
#         res += i
#     return res

# a = sum_numbers(5, 10)
# print(a)

# v2
# def sum_numbers(n, y = 'bye-bye'):
#     print(y)
#     res = 0
#     for i in range(1, n + 1):
#         res += i
#     print(res)

# sum_numbers(5, 10)

# принимать и передовать неограниченное кол-во аргуметов с помощью *
# def sum_string(*args):
#     res = ''
#     for i in args:
#         res += str(i)
#     return res

# print(sum_string('g', 'a', 'n', 'd', 'u', 'r', 'a', 's'))
# print(sum_string('б', 'р', 'ы', 'с', 'ь',))
# print(sum_string(1,5,6,2,))

# def max1(a, b):
#     if a > b:
#         return a
#     return b
# print(max1(5,9))

# #обращаемся/импортируем к функции из другого модуля
#import modul1 
# #вызываем конкретную функцию и присваиваем значения переменных
#print(modul1.maxElem(5, 9))

# from modul1 import maxElem # from modul1 import * # импортировать все функции
# print(maxElem(15,9))

# import modul1 as m1
# print(m1.maxElem(15,8))

#функция вывода числа Фибоначи
# Числа Фибоначчи - это последовательность чисел, в которой каждое число
# является суммой двух предыдущих чисел. Формально, если мы обозначим
# числа Фибоначчи как F(n), то F(0) = 0, F(1) = 1, и для всех n >= 2, F(n) = F(n-1) + F(n-2).
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# # def fibonacci(n):
# #     if n <= 1:
# #         return n
# #     else:
# #         return fibonacci(n-1) + fibonacci(n-2)
# # def fibonacci_iterative(n):
# #     fib = [0, 1]
# #     for i in range(2, n+1):
# #         fib.append(fib[i-1] + fib[i-2])
# #     return fib[n]

# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
    
# # print(list1)

# def quickSort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
   
#     return quickSort(less) + [pivot] + quickSort(greater)

# print(quickSort([1,3,7,9,4,33,7,90]))

# def MergeSort(nums):
#     if len(nums) > 1:
#         midlle = len(nums) // 2
#         left = nums[:midlle]
#         right = nums[midlle:]
#         MergeSort(left)
#         MergeSort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [4,66,34,9,60,6,0,3,]       
# MergeSort(list1)
# print(list1)     

#Последовательность Фибоначчи, найти n
# 0 1 1 2 3 5 8 13 21 - чмсла фибоначчи

# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input())
# print(fib(n-2))

#заменить максимальное число на максимальное в массиве

# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)

# max_n = max(list1)
# min_n = min(list1) 

# for i in range(len(list1)):
#     if list1[i] == max_n:
#         list1[i] = min_n

# print(list1)

#если число делится на себя и на 1 то - интересное (да)

# def Prime(n):
#     flag = True
#     i = 2
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#         if flag:
#             return "yes"
#         return 'no'
    
# n = 21
# print(Prime(n))

# def is_prime(n):
#     if n <= 1:
#         return False  # Числа меньше или равные 1 не являются простыми
#     for i in range(2, int(n**0.5) + 1):  
#         # Проверяем делители от 2 до квадратного корня из n
#         # n ** 0.5 вычисляет квадратный корень из числа n.
#         # int(n ** 0.5) берет только целую часть квадратного корня.
#         # + 1 добавляет 1 к целой части, чтобы охватить последний элемент диапазона.
#         # range(2, int(n ** 0.5) + 1) создает последовательность чисел от 2 до целой части квадратного корня из n, включительно.
#         if n % i == 0:
#             return False  # Если находим делитель, число не простое
#     return True  # Если ни один делитель не найден, число простое

# # Ввод числа с клавиатуры
# num = int(input("Введите число для проверки: "))
# print(num**0.5)
# if is_prime(num):
#     print(num, "является простым числом")
# else:
#     print(num, "не является простым числом")

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n-1) + f'{k}'

# n = int(input())
# print(f(n))

# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

def f(a,b):

    res = a ** b
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a * f(a, -b - 1)) # Обрабатываем отрицательные степени
    else:
        return a * f(a, b -1)

a = int(input())
b = int(input())
result = f(a,b)
print(result)

#f'{res} = {a ** b}\n'
#f'{res} = {a ** b}\n' используется для форматирования строки.
# Здесь \n - это специальный символ, который обозначает перевод
# строки. Он добавляет новую строку после каждой строки вывода,
# что делает вывод более читаемым, разделяя каждое уравнение на новой строке.

