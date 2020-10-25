#python中用**表示乘方运算
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

#数字列表统计计算
print(min(squares))
print(max(squares))
print(sum(squares))

#列表解析 变量名=[表达式 for循环]
squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)