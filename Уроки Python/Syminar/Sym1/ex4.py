# Напишите программу, которая  будет принимать на вход дробь и показывает первую цифру дробной части чмсла.
# -> 6,78 --> 7
# -> 5 --> Нет
# -> 0,34 --> 3

y = float(input(" Введите дробное число --> "))
if int(y) == y:
    print(" Нет номер не дробный ")
else:
    print(int(y*10) % 10)

# y = (input(" Введите дробное число --> "))
# print(y.split(",")[1][0])