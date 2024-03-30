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
    
# print(list1)

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
   
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([1,3,7,9,4,33,7,90]))

    