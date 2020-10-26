filename = 'programming.txt'
# 写入文件，参数w为写入，a为添加
with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")