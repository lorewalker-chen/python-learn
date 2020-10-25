#利用input()函数获取用户输入
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
#利用while循环让用户选择退出程序时机
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)