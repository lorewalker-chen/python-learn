bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#访问列表元素,利用[]
print(bicycles[0])
#索引指定为-1返回列表中最后一个元素,-2返回倒数第二个，以此类推
print(bicycles[-1])
#使用列表元素
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)