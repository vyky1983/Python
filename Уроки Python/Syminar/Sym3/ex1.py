# n = 9
# while k:=len(input('-->').split()) == n:
#     print('Пробуй ещё раз')

print(' --------------->')  

def fun(a_1, a_2, *args, **kwargs):
    return a_1, a_2, args, kwargs
print(fun(a_1=3, a_2=5,))

print(' --------------->')  

def fun(a_1: list[int|str]) ->tuple:   #Type Hinting то механизм, который позволяет явно указывать типы параметров. Интерпретатор использует их и применяет исключение в тех ситуациях, когда тип не соответствует ожидаемому. 
    return a_1, 
print(fun(a_1=123,))