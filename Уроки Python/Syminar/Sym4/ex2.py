# 2. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9

import pathlib
a = '1 2 3 4 5 6 7 9'

with open('number.txt', 'w') as data:
    data.write(a)

with open('number.txt', 'r') as data:
    lst = a.split()
    for i in range(1,len(lst)):
        # print(lst[i])
        if (int(lst[i]))-1 != (int(lst[i-1])):
            print(int(lst[i])-1)



# with open(file_path, 'r') as f:
#     list_new = list(map(int, f.read().split()))
#     list_new = [list_new[i]+1 for i in range(len(list_new)-1) if
# От ViktoriaAmster всем 11:50 AM
# for i in range(1, len(list_)):
#         if list_[i] - 1 != list_[i - 1]:
#             print(list_[i-1] + 1)

# fileText = r'secondfile.txt'
# with open(fileText, 'r') as ourFile:
#     strlist = ourFile.read().split(' ')

# x = list(map(int, strlist))
# searchNum(x)
