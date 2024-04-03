# посчитать кол-во уникальных чисел в списке
# list = [1,1,2,3,5,5]
# print(len(set(list)))

#сдвинуть послдовательность чисел N на К элементов

# list1 = [5,4,6,7,-10]
# k = int(input())
# k = k % len(list1)

# list_res = []
# for i in range(k):
#     list_res.append(list1[len(list1) - 1 - i])
# print(list_res)

# for i in range(len(list1) - k):
#     list_res.append(list1[i])
# print(list_res)

# list1 = [5,4,6,7,-10]
# k = int(input())
# k = k % len(list1)
# print(k)

# вывести все уникальные данные в словаре
# list = [{"V": "s001"}, {"V": "s002"}, {"VI": "s001"}, {"VI": "s005"}, {"VII": "s005"}, {"V": "s009"}, {"VIII": "s007"}]
# set1 = set()
# for i in list:
#     for j in i:
#         set1.add(i[j])
# print(set1)

# посчитать кол-во элементов массива, 
# если элемент больше предыдущего

# list2 = [0, -1, 5,2,3 ]
# count = 0

# for i in range(1, len(list2)):
#     if list2[i] > list2[i-1]:
#         count += 1
# print(count)

#сколько раз встречается чисто К в массиве?
# list_1 = [1, 2, 3, 4, 5]
# k = int(input())
# count = 0

# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)
# # Требуется найти в массиве list_1 самый близкий по значению 
# элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# #sort_list_1 = sorted(list_1)
# list2 = []
# list3 =[]
# res_item = 0
# min_val = 0
# max_val = 0

# for i in range(len(list_1)):
#     if k >= list_1[i]:
#         list2.append(list_1[i])
#         min_val = max(list2)
#     if k < list_1[i]:
#         list3.append(list_1[i])
#         max_val = min(list3)

# if min_val > max_val or max_val - k > k - min_val:
#     res_item = min_val
    
# else:
#     if max_val - k < k - min_val:
#         res_item = max_val
    
# print(list2, list3)
# print(min_val, max_val)
# print(res_item)

# вывести ближайший к числу К элемент из списка list_1  
# list_1 = [10, 12, 7, 44, 89]
# k = 16
# res_item = list_1[0]
# min_val = abs(k - list_1[0])

# for i in range(len(list_1)):
#     if min_val >= abs(k- list_1[i]):
#         res_item = list_1[i]
# print(res_item)

# Скрабл: каждой букве присвоить кол-во очков. 
# Посчитать сколько очков наберет введенное слово

# scrabbleUK = list(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z'])
# scrabbleRUS = list(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'Д', 'К', 'Л', 'М', 'П', 'У', 'Б', 'Г', 'Ё', 'Ь', 'Я', 'Й', 'Ы', 'Ж', 'З', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Ф', 'Щ', 'Ъ'])
# generalScrabble = set(scrabbleUK + scrabbleRUS)

# k = "ноутбук".upper()
# count = 0
# score1 = set(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'])
# score2 = set(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'])
# score3 = set(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я',])
# score4 = set(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы',])
# score5 = set(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч',])
# score8 = set(['J', 'X', 'Ш', 'Э', 'Ю',])
# score10 = set(['Q', 'Z', 'Ф', 'Щ', 'Ъ'])

# for j in range(len(k)):
#     if k[j] in generalScrabble:
#         if k[j] in score1:
#             count += 1
#         if k[j] in score2:
#             count += 2
#         if k[j] in score3:
#             count += 3
#         if k[j] in score4:
#             count += 4
#         if k[j] in score5:
#             count += 5
#         if k[j] in score8:
#             count += 8
#         if k[j] in score10:
#             count += 10
           
# print(k)
# print(count)

# #print(* scrabble)

# version2

# k = input()
# res = 0
# k = k.upper()
# score1 = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
# score2 = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
# score3 = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я',}
# score4 = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы',}
# score5 = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч',}
# score8 = {'J', 'X', 'Ш', 'Э', 'Ю',}
# score10 = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}

# selection1 = dict.fromkeys(score1, 1)
# selection2 = dict.fromkeys(score2, 2)
# selection3 = dict.fromkeys(score3, 3)
# selection4 = dict.fromkeys(score4, 4)
# selection5 = dict.fromkeys(score5, 5)
# selection8 = dict.fromkeys(score8, 8)
# selection10 = dict.fromkeys(score10, 10)
# selection = {**selection1, **selection2, **selection3, **selection4, **selection5, **selection8, **selection10}

# for j in k:
#     for i in selection:
#         if j == i: res = res + selection[i]

# print(res)


# Ввести строки и посчитать сколько раз свтречается буква в  списке

# string = input().split()  #преобразовать строку в массив данных
# res = {}                  #словарь, в который будем помещать значения

# for i in string:
#     if i in res:
#         print(f'{i}_{res[i]}', end =' ')
#     else:
#         print(i, end =' ')
#     res[i] = res.get(i, 0) + 1    
#     #функция обращается к ключу i, если его нет то присвоить 0. 
#     # Если на вход поступает новая буква и ее нет в словаре, 
#     # то результат = 0, если буква есть то к ней добавляеся 1

#Посчитать количество пробелов в тексте
# string = input().split()
# set1 = set()

# for i in string:
#     set1.add(i.lower())

# print(len(set1))

# проверить 2 кода на кол-во ошибок, побеждает тот код, 
# в котором ошибок меньше

# var1 = '4 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел

# # преобразование списка в множество set с помощью функции .split
# # .split() разбивает строку '5 4' на две подстроки '5' и '4'
# # и возвращает их в виде списка, содержащий элементы этой строки.
# var1_set = var1.split()

# # set() создает множество из полученного списка, удаляя все повторяющиеся элементы,
# # чтобы оставить только уникальные значения.
# var2_set = set(var2.split())
# var3_set = set(var3.split())

# # преобразование множетсва в массив
# var1_array = [int(num) for num in var1_set]  

# n = var1_array[0]
# m = var1_array[1]


# print(var1_array)
# print(var2_set)
# print(var3_set)
# # сравнение множетсв и вывод только тех элем., которые есть в обоих мн-ах
# result = var2_set.intersection(var3_set)
# result = sorted(result)
# # .join() объединяет элементы списка в строку, используя строку,
# # к которой он применяется, в качестве разделителя между элементами.

# print(' '.join(result))
    
# arr = [2, 4, 10, 4, 2]
# res = []
# count = 0


# #while count < len(arr) -1:
    
# for i in range(1, len(arr) -1):
#     current_sum = arr[i] + arr[i-1] + arr[i+1]
#     res.append(current_sum)

# max_cell = res[0]

# for j in range(1, len(res)):    
#     if res[j] > max_cell:
#         max_cell = res[j]
# count +=1
# print(res)
# print(max_cell)

arr = [2, 4, 10, 4, 2]
midlle = len(arr) // 2
left = arr[:midlle]
right = arr[midlle:]
print(arr[midlle])
print(left)
print(right)