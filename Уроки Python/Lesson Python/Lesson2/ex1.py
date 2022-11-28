# color = ("red", "gren", "blue3")
# data = open("file.txt", "w")
# #data.writelines(color)  # Разделителей не будет
# data.write("\nLINE 312\n")
# data.write("\nLINE 513\n")
# data.close()


path = "file.txt"
data = open(path, "r")
for line in data:
    print(line)
data.close()

exit()