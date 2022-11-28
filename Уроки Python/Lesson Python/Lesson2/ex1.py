color = ("red", "gren", "blue")
data = open("file.txt", "a")
data.writelines(color)  # Разделителей не будет
# data.write("\nLINE 312\n")
# data.write("\nLINE 513\n")
data.close()

exit()
path = "file.txt"
data = open(path, "r")
for line in data:
    print(line)
data.close()