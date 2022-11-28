list1 = [1, 2, 3, 4, 5]
list2 = list1

print(list1.pop(2))
print(list1.insert(2, 11))
print(list1.append(15))
print(len(list1))


for k in list1:
    print(k)

print()

for i in list2:
    print(i)


list1[0] =123
list2[1]=333
for k in list1:
    print(k)

print()

for i in list2:
    print(i)
