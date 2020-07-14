name1 = "ada lovelace"
print(name1.title())  # 首字母大写
print("*********************")
# 大小写转换
name2 = "Ada Lovelace"
print(name2.upper())  # 全部转大写
print(name2.lower())  # 全部转小写
print("*********************")
# 拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)
print("*********************")
# 制表符和换行符
print("Python")
print("\tPython")
print("Laguages:\nPthon\nC\nJavaScript")
print("Laguages:\n\tPthon\n\tC\n\tJavaScript")
print("*********************")
# 删除空白
favorite_language = " python "
favorite_language.lstrip()  #删除开头空白
favorite_language.rstrip()  #删除末尾空白
favorite_language = favorite_language.strip()  #删除两端空白
print(favorite_language)