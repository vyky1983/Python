# Напишите программу, в которой пользователь будет задовать две строки, а программа определит количество вхождений одной строки.

text = 'Я люблю Python люлюлюлюлюлю'

char = input('Введите значение поиска: ')
len_char = len(char)
i = 0
count = 0
while i < len(text)-1:
    if char.lower() == text[i:len_char+i].lower():
        count += 1
    i += 1
print(count )
