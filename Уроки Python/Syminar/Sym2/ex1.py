# Напишите программ, которая принимает на вход чмсло N и выдает последовательность из N чисел
# Примиер
# Для n 5: 1, -3, 9, -27 ,81.

# n = int(input('Введите число n --> '))

# for x in range(n):
#     result = (-3)**x
#     print(result, end=' ')


n = int(input('Введите число --> ' ))

# for i in range(n):
#  result= (-3)**i
#  print(result, end=' ')

i=0
while i<n:
 print((-3)**i, end=(' '))
 i+=1

