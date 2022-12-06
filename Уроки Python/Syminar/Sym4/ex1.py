# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'

# my_str='Я люблю Джавуабв абви Питон'
# lst =my_str.split(' ')
# print(lst)
# my_list=[]
# for i in lst:
#     if "aba" in i:
#      my_list.append
# print(my_list)

my_str = 'Я люблю Джавуабв абви Питон'
lst = my_str.split(" ")
my_list = [i for i in lst if "абв" not in i]
print(*my_list)

print("------------->")

string = 'Я люблю Джавуабв абви Питон'
s1 = 'абв'
print(' '.join([i for i in string.split() if i.count(s1) == 0]))

