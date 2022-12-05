from typing import Any

def sum(x): return x+10


def mult(x): return x**2


print(sum(mult(2)))
print()

print('1------------>')


def sum1(x): return x+22


def mult2(x): return x**3


print(sum1(mult2(2)))
print()

print('2------------>')


def sum4(x): return x+242


def mult4(x): return x**5


print(sum4(mult4(2)))
print()

print('3------------>')


# def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))


# h(lambda x: x+10, lambda x: x**2, 5)
