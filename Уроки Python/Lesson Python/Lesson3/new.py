# path = "file.txt"
# data = open(path, "r")
# for line in data:
#     print(line)
# data.close()

# exit()
path = "file.txt"
f = open(path, 'r')
f.write("\n 1 2 3 5 8 15 23 38\n")
data = f.read()+" "
f.close()
# exit()

#
numbers = []

while data != '':
    space_pos = data.index(" ")
    numbers.append(int(data[:space_pos]))
    data = data[:space_pos+1]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)

f = open('f.txt', 'r')
data = f.read() + ' '
f.close()
numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)


print("------------>")

# Анонимные, lambda функции


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))

print("------------>")

#Анонимные, lambda функции

def select(f, col):
 return [f(x) for x in col]
def where(f, col):
 return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))

print("------------>")

#Анонимные, lambda функции

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)
