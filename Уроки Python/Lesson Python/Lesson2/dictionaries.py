dictionaries = {}
dictionaries = \
    {
       'up': '↑',
       'left': '←',
       'down': '↓',
       'right': '→'
    }
# print(dictionaries)
# print(dictionaries['left'])

# for k in dictionaries.keys():
#  print(k)

# for k in dictionaries.values():
#  print(k)

for v in dictionaries:
 print(v)
 print(dictionaries[v])

dictionaries['up']= 125
print(dictionaries['up'])
