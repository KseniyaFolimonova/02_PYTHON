# сложные функции. LAMBDA
# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x,y))

# #def calk1(a,b):
#     #return a+b

# calk1 = lambda a,b: a+b
# math(calk1, 5, 45) 


# def select(f, col):
#     return [f(i) for i in col] # просто перебирает и вводит список, который подан на ввод

# def where(f, col):
#     return[i for i in col if f(i)] #перебирает список и проверяет на какое-то условие

# data = [1,4,6,8,3,5,6] # поданный список
# res = select(int, data) # список результата с типом данных
# print(res)
# res = where(lambda i: i % 2 == 0, res) # добавление условия в функцию where
# print(res)
# res = list(select(lambda i: (i, i*i), res)) # присоение списку КОРТЕЖ и вывод элементов с квадратом числа
# print(res)

# сложные функции. MAP

# list1 = [i for i in range (0, 20)]
# print(list1)

# list1 = list(map(lambda i: i + 10, list1)) # функция в которой мы передаем 2 параметра: функцию которую применяем к объекту и сам объект
# print(list1)

# data = '8 93 61 5 23 10 4'
# print(data)                 # 8 93 61 5 23 10 4

# data = list(data.split())
# print(data)                 # ['8', '93', '61', '5', '23', '10', '4']

# data = list(map(int, data.split()))
# print(data)                 # [8, 93, 61, 5, 23, 10, 4]


# def where(f, col):
#     return[i for i in col if f(i)] 

# data = [1,4,6,8,3,5,6] 
# res = map(int, data) 
# print(res)

# res = where(lambda i: i % 2 == 0, res) 
# print(res)

# res = list(map(lambda i: (i, i*i), res)) 
# print(res)

# сложные функции. FILTER

# data = [1,4,6,8,3,5,6]
# res = list(filter(lambda x: x % 2 != 0, data))
# print(res)


# data = [1,4,6,8,3,5,6] 
# res = map(int, data)                     # преобр. список в список/массив
# res = filter(lambda i: i % 2 == 0, res)  # фильтр преобр-го элемен. списка на кратность 2
# res = list(map(lambda i: (i, i*i), res)) # функция преобр. элемен. списка в квадрат и вывод кортежем
# print(res)

# функция ZIP

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4,5,7,9,1]
# data = list(zip(users, ids))
# print(data)                  #[('user1', 4), ('user2', 5), ('user3', 7), ('user4', 9), ('user5', 1)]


# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4,5,7,9,1,10]
# salary = [111,333,222,8,5,3]
# data = list(zip(users, ids, salary))
# print(data)                  # [('user1', 4, 111), ('user2', 5, 333), ('user3', 7, 222)]

# функция ENUMERATE
# citys = ['Kazan', 'Smolensk', 'Chicago', 'Moskow']
# list1 = list(enumerate(citys))
# print(list1)

# colors = ['red', 'ponpi-up', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# print(56)

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

# transfomation = lambda x: x
# values = [2,5,6,7,9,12,45,87,54]
# transformed_values = list(map(transfomation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# from math import pi

# def find_farthest_orbit(list_of_orbits):
#     list1 = [i for i in list_of_orbits if i[0] != i[1]]
#     print(list1)
#     list_s = [(pi * i[0] * i[1]) for i in list1]  # считаем площадь каждой орбиты и пробигаемся по всему массиву списка
#     max_s = list_s.index(max(list_s))             # вытаскиваем индекс максимального значения из списка

#     print(list1[max_s])
#     return list_s[max_s]

# orbits = [(1,2), (9.8,10), (2.6,7), (5,5), (3,4)]
# print(find_farthest_orbit(orbits))
# #find_farthest_orbit(orbits)

# def same_by(characteristic, object):
#     result = True
#     list1 = [characteristic(x) for x in object]
#     for i in range(len(list1) - 1):
#         if list1[i] != list1[i+1]:
#             result = False
#     return result


# value = [2,5,0,61]
# if same_by(lambda x: x % 2, value):
#     print('same')
# else:
#     print('different')

    
# def print_operation_table(operation, num_rows = 9, num_columns = 9):
        
#     if num_rows <= 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return  
    
#     for row in range(1, num_rows+1):
#         list1 = []
#         for col in range(1, num_columns+1):
#             list1.append(operation(row,col)) #print(f"{operation(row, col):<2}", end=" ")
#         print(*list1)

# print_operation_table(lambda x, y: x *y, 3,3)

# def print_operation_table(operation, num_rows = 9, num_columns = 9): 
#     if num_rows < 2: 
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!') 
#     else: 
#         for i in range(num_rows): 
#             lst = [] 
#             for j in range(num_columns): 
#                 lst.append(operation(i+1,j+1)) 
#             print(*lst) 
  
# print_operation_table(lambda x, y: x * y, 3, 3)


