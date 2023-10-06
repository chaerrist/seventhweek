# ##Big(O) - O(n) 코드 작성
# # arr = [0, 1, 2, 3, 4, 5]

# # def ret_O1(idx) :
# #     return arr[idx]

# # print(ret_O1(2))

# ## import time
# # arr = [1, 2, 3, 4, 5]

# # def ret_O1(idx) :
# #     return arr[idx]

# # start = time.time()
# # print(ret_O1(2))
# # end = time.time()
# # print(f"{end - start : 5f} sec")


# import time
# arr = [1, 2, 3, 4, 5]

# def print_elements(arr):
#     for elem in arr:
#         print(elem)

# start = time.time()      
# print_elements(arr)
# end = time.time()

# print(f"{end - start : 5f} sec")

# ##O(log(n))

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     print(left, right)
    
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return -1

# my_list = [1, 2, 3, 4, 5]

# result = binary_search(my_list, 4)
# if result != -1:
#     print(f"요소가 {result}번째 인덱스에 있습니다.")
# else:
#     print("요소를 찾을 수 없습니다.")
    
    
# ##O(2n)

# def mul_for():
#     for i in range(5):
#         for j in range(5):
#             print(i,j)
            
# start = time.time()      
# mul_for()
# end = time.time()

# print(f"{end - start : 5f} sec")


# ## 버블 정렬

# def bubble_sort(arr):
#     N = len(arr)
#     for i in range(N):
#         # print(i, arr)
#         for j in range(N-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1], arr[j]
#             print(i, j, arr, arr[i], arr[j])
#     return arr

# lrr = [1, 9, 2, 7, 5]
# print(bubble_sort(lrr))

# ## 퀵 소트 

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     piv = arr[len(arr) // 2]
#     left = [x for x in arr if x < piv]
#     mid = [x for x in arr if x == piv]
#     rgt = [x for x in arr if x > piv]
#     print("pivot : %s, left : %s, middle : %s, right : %s" %(piv, left, mid, rgt) )
    
#     return quick_sort(left) + mid + quick_sort(rgt)

# my_list = [1, 9, 6, 4, 5, 7, 3, 2]
# print(len(my_list))

# sorted_list = quick_sort(my_list)

# print(sorted_list)

## pip - requests module

# import requests

# res = requests.get('https://www.google.com/')
# print(res)
# print(res.content)


# import numpy as np

# a = np.array([1, 2, 3])
# print(a)

# b = np.zeros([2, 3])
# print(b)

# c = np.ones([2, 3])
# print(c)

# d = np.array([1, 2, 3])
# e = np.array([4, 5, 6])

# f = d + e
# g = d - e
# h = d * e
# i = d / e

# print(f, "\n", g, "\n", h, "\n", i)

# import pandas as pd

# data = {'Name': ['John', 'Jane', 'Mike', 'Sarah'],
#         'Age': [25, 30, 35, 40],
#         'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

# df = pd.DataFrame(data)
# print(df)

# # print(df['Age'].describe())

# print(df.sort_values(by='Age', ascending = False))
# print("=================")
# print(df.sort_values(by='Age', ascending= True))
# print("=================")
# print(df.sort_values(by='Name', ascending=True))

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.plot(x, y)

plt.xlabel('time')
plt.ylabel('n')
plt.title('Example plot')

plt.show()