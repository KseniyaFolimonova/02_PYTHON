# n = int(input('введите размер первого массива: '))
# arr1 = list()
# for i in range(n):
#     x = int(input())
#     arr1.append(x)

# m = int(input('введите размер второго массива: '))
# arr2 = list()
# for j in range(m):
#     x = int(input())
#     arr2.append(x)

# count = 0
# for i in range(n):
#     for j in range(m):
#         if arr1[i] == arr2[j]:
#             count += 1
#     if count == 0:
#         print(arr1[i])
#     count = 0

# n = (4,5,7,3,4,5)
# list1 = list()
# for a in n:
#     list1.append(a)
# count = 0
# for i in range(1,len(list1) - 1):
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count += 1 
# print(count)

# list1 = [1,2,5,9,2,6]
# count = 0

# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if i != j and list1[i] == list1[j]:
#             count += 1
# print(count)

k = int(input())
list1 = list()

for i in range(k):
    summa = 0
    for j in range(1, i//2 + 1):
        if i % j == 0:
            summa += j
    list1.append(tuple([i, summa]))

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
            print(*list1[i]) 