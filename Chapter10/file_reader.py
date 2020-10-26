# 读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print("*****************")
# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())