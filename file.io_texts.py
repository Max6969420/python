f = open("file.txt")
content = f.read()
print(content)
# content = f.read(2) READS ONLY 2 CHARACTER
# content = f.read(34354)
# print("1", content)
# content = f.read(23243)
# print("2", content)
# for line in content:
#         print(line)
for line in f:
    print(line, end="")

f.close()
