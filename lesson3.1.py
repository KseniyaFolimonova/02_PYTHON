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

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()