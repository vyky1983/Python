color = ("red", "gren", "blue")
data = open("file.txt", "w")
data.writelines(color)  # Разделителей не будет
data.close()

exit()
path = "file.txt"
data = open(path, "r")
for line in data:
    print(line)
data.close()